#!/usr/bin/env python3
"""Collect registered public threads and publisher audio; optionally transcribe it."""

import argparse
import datetime as dt
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET


class ThreadParser(HTMLParser):
    """Read attributed posts only, excluding recommendations and page boilerplate."""

    def __init__(self):
        super().__init__()
        self.posts = []
        self.current = None
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.current is None:
            if (tag == "div" and "content-tweet" in attrs.get("class", "").split()
                    and attrs.get("data-screenname") == "nikitabier"
                    and attrs.get("data-tweet", "").isdigit()):
                self.current = {"id": attrs["data-tweet"], "parts": []}
                self.depth = 1
        elif tag == "div":
            self.depth += 1
        elif tag == "br":
            self.current["parts"].append("\n")

    def handle_endtag(self, tag):
        if self.current is not None and tag == "div":
            self.depth -= 1
            if self.depth == 0:
                post = self.current
                self.current = None
                text = "\n".join(line.strip() for line in
                                 "".join(post.pop("parts")).splitlines() if line.strip())
                post.update(text=text, url="https://x.com/nikitabier/status/" + post["id"])
                milliseconds = (int(post["id"]) >> 22) + 1288834974657
                post["date"] = dt.datetime.fromtimestamp(
                    milliseconds / 1000, dt.timezone.utc).isoformat().replace("+00:00", "Z")
                self.posts.append(post)

    def handle_data(self, data):
        if self.current is not None:
            self.current["parts"].append(data)


def digest(path):
    with path.open("rb") as stream:
        return hashlib.sha256(stream.read()).hexdigest()


def fetch(url, path):
    partial = path.with_suffix(path.suffix + ".part")
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=45) as response, partial.open("wb") as out:
            shutil.copyfileobj(response, out)
    except Exception:
        if not shutil.which("curl"):
            partial.unlink(missing_ok=True)
            raise
        try:
            subprocess.run(["curl", "-sSfL", "--retry", "1", "--connect-timeout", "15",
                            "--max-time", "120", "-A", "Mozilla/5.0", "-o", str(partial), url],
                           check=True, timeout=260, capture_output=True)
        except Exception:
            partial.unlink(missing_ok=True)
            raise
    if not partial.stat().st_size:
        partial.unlink()
        raise ValueError("Empty response")
    partial.replace(path)


def audio_duration(path):
    if not shutil.which("ffprobe"):
        raise RuntimeError("ffprobe is required to verify the downloaded audio")
    data = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
                                    "format=duration", "-of", "json", str(path)], text=True)
    duration = float(json.loads(data)["format"]["duration"])
    if duration <= 0:
        raise ValueError("Invalid audio duration")
    return duration


def transcribe(path, destination, model):
    import mlx_whisper  # Optional: used only with --transcribe.
    result = mlx_whisper.transcribe(str(path), path_or_hf_repo=model,
                                   language="en", verbose=None)
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"model": model, "words": len(result["text"].split()),
            "segments": len(result["segments"]), "sha256": digest(destination),
            "speaker_attribution": "not_diarized", "human_audio_verified": False}


def collect(source, output, args):
    source_dir = output / source["id"]
    source_dir.mkdir(parents=True, exist_ok=True)
    record = {"id": source["id"], "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
              "url": source["url"], "status": "failed"}
    try:
        if source["kind"] == "thread":
            page = source_dir / "page.html"
            if args.refresh or not page.exists():
                fetch(source["url"], page)
            parser = ThreadParser()
            parser.feed(page.read_text(encoding="utf-8"))
            posts = parser.posts
            if not posts or len({post["id"] for post in posts}) != len(posts):
                raise ValueError("No attributed posts or duplicate post IDs")
            if len(posts) != source["expected_posts"]:
                raise ValueError("Thread length changed; inspect before counting it")
            for post in posts:
                post.update(source_id=source["id"], access="thread_mirror")
            text_path = source_dir / "posts.jsonl"
            text_path.write_text("".join(json.dumps(post, ensure_ascii=False) + "\n"
                                         for post in posts), encoding="utf-8")
            record.update(status="collected", records=len(posts),
                          text_words=sum(len(post["text"].split()) for post in posts),
                          page_sha256=digest(page), text_sha256=digest(text_path))
        else:
            feed_path = source_dir / "feed.xml"
            if args.refresh or not feed_path.exists():
                fetch(source["feed_url"], feed_path)
            matches = [item for item in ET.fromstring(feed_path.read_bytes()).findall(".//item")
                       if item.findtext("title") == source["episode_title"]
                       and source["publication_date"] in (item.findtext("pubDate") or "")]
            if len(matches) != 1:
                raise ValueError("Expected one dated episode in publisher RSS")
            item = matches[0]
            audio_url = item.find("enclosure").attrib["url"]
            audio = source_dir / "audio.mp3"
            if args.refresh or not audio.exists():
                fetch(audio_url, audio)
            record.update(status="collected", audio_url=audio_url,
                          duration_seconds=audio_duration(audio), audio_bytes=audio.stat().st_size,
                          audio_sha256=digest(audio), feed_sha256=digest(feed_path))
            if args.transcribe:
                record["asr"] = transcribe(audio, source_dir / "asr.json", args.asr_model)
        (source_dir / "result.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    except Exception as error:
        record.update(status="failed", error=f"{type(error).__name__}: {error}")
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source", action="append", help="Source ID; repeat to select several")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--transcribe", action="store_true", help="Requires mlx-whisper and a model")
    parser.add_argument("--asr-model", default="mlx-community/whisper-large-v3-turbo")
    args = parser.parse_args()
    manifest = Path(__file__).resolve().parents[1] / "references" / "acquisition-manifest.json"
    sources = json.loads(manifest.read_text(encoding="utf-8"))["sources"]
    known = {source["id"] for source in sources}
    if args.source and set(args.source) - known:
        parser.error("Unknown source IDs: " + ", ".join(sorted(set(args.source) - known)))
    args.output.mkdir(parents=True, exist_ok=True)
    selected = [source for source in sources if not args.source or source["id"] in args.source]
    records = []
    for source in selected:
        record = collect(source, args.output, args)
        records.append(record)
        print(json.dumps(record), flush=True)
    (args.output / "collection-results.json").write_text(json.dumps(records, indent=2), encoding="utf-8")
    return int(any(record["status"] == "failed" for record in records))


if __name__ == "__main__":
    sys.exit(main())
