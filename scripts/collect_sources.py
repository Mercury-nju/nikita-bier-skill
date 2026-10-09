#!/usr/bin/env python3
"""Collect public posts, publisher articles/audio, and exported video captions."""

import argparse
import datetime as dt
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
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


class ArticleParser(HTMLParser):
    """Extract the registered article container, excluding surrounding navigation."""

    def __init__(self, container_class):
        super().__init__()
        self.container_class = container_class
        self.container_tag = None
        self.depth = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.depth and tag == self.container_tag:
            self.depth += 1
        elif not self.depth and self.container_class in attrs.get("class", "").split():
            self.container_tag = tag
            self.depth = 1
        if self.depth and tag in ("p", "br", "h2", "h3", "li"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if self.depth and tag == self.container_tag:
            self.depth -= 1
        if self.depth and tag in ("p", "h2", "h3", "li"):
            self.parts.append("\n")

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)

    def text(self):
        return "\n".join(" ".join(line.split()) for line in
                         "".join(self.parts).splitlines() if line.strip())


def parse_captions(path, source):
    """Validate a browser export against its video ID and observed final cue."""
    raw = path.read_text(encoding="utf-8")
    if "Video ID: " + source["video_id"] not in raw.splitlines():
        raise ValueError("Caption export does not match the registered video ID")
    segments = []
    for line in raw.splitlines():
        match = re.fullmatch(r"\[(\d+:\d{2}(?::\d{2})?)\]\s+(.+)", line)
        if not match:
            continue
        seconds = 0
        values = match[1].split(":")
        if any(int(value) >= 60 for value in values[1:]):
            raise ValueError("Invalid caption timestamp")
        for value in values:
            seconds = seconds * 60 + int(value)
        if segments and seconds < segments[-1]["start"]:
            raise ValueError("Caption timestamps are not monotonic")
        segments.append({"start": seconds, "text": match[2]})
    if not segments or segments[-1]["start"] < source["minimum_last_cue_seconds"]:
        raise ValueError("Caption export is empty or ends before the observed final cue")
    if segments[-1]["start"] > source["duration_seconds"]:
        raise ValueError("Caption timestamp exceeds registered video duration")
    return segments


def digest(path):
    with path.open("rb") as stream:
        return hashlib.sha256(stream.read()).hexdigest()


def parse_proxy_post(path, expected_id):
    """Check the requested post identity without claiming original-page access."""
    response = json.loads(path.read_text(encoding="utf-8"))
    post = response.get("tweet") or {}
    if (response.get("code") != 200 or str(post.get("id")) != expected_id
            or post.get("author", {}).get("screen_name", "").lower() != "nikitabier"):
        raise ValueError("Proxy response has the wrong post ID, author, or status")
    text = post.get("text", "").strip()
    if not text or all(part.startswith("@") for part in text.split()):
        raise ValueError("No substantive text; review mentions-only/media records separately")
    milliseconds = (int(expected_id) >> 22) + 1288834974657
    if int(post.get("created_timestamp", -1)) != milliseconds // 1000:
        raise ValueError("Proxy date disagrees with the post ID")
    return {"id": expected_id, "url": "https://x.com/nikitabier/status/" + expected_id,
            "date": dt.datetime.fromtimestamp(milliseconds / 1000, dt.timezone.utc)
                      .isoformat().replace("+00:00", "Z"),
            "text": text, "access": "third_party_x_json",
            "replying_to_status": post.get("replying_to_status"),
            "media_present": bool(post.get("media")),
            "quote_url": (post.get("quote") or {}).get("url")}


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
        elif source["kind"] == "x_proxy":
            posts, hashes = [], {}
            if (not source["post_ids"]
                    or len(set(source["post_ids"])) != len(source["post_ids"])):
                raise ValueError("Empty or duplicate registered post IDs")
            for post_id in source["post_ids"]:
                response_path = source_dir / (post_id + ".json")
                if args.refresh or not response_path.exists():
                    fetch(source["provider_base_url"] + post_id, response_path)
                post = parse_proxy_post(response_path, post_id)
                post["source_id"] = source["id"]
                posts.append(post)
                hashes[post_id] = digest(response_path)
            text_path = source_dir / "posts.jsonl"
            text_path.write_text("".join(json.dumps(post, ensure_ascii=False) + "\n"
                                         for post in posts), encoding="utf-8")
            record.update(status="collected", records=len(posts),
                          acquisition="third_party_x_json",
                          provider_base_url=source["provider_base_url"],
                          text_words=sum(len(post["text"].split()) for post in posts),
                          response_sha256=hashes, text_sha256=digest(text_path),
                          original_page_verified=False, attached_media_reviewed=False)
        elif source["kind"] == "youtube_captions":
            captions = source_dir / "captions.txt"
            supplied = args.caption_files.get(source["id"])
            if supplied:
                # Validate before replacing a previously usable local export.
                parse_captions(supplied, source)
                if supplied.resolve() != captions.resolve():
                    shutil.copyfile(supplied, captions)
            elif args.refresh or not captions.exists():
                raise ValueError("Export the official video's transcript, then provide "
                                 "--caption-file " + source["id"] + "=/absolute/path.txt")
            segments = parse_captions(captions, source)
            parsed = source_dir / "captions.json"
            parsed.write_text(json.dumps(segments, ensure_ascii=False, indent=2), encoding="utf-8")
            record.update(status="collected", acquisition="browser_transcript_export",
                          duration_seconds=source["duration_seconds"],
                          caption_words_all_speakers=sum(len(s["text"].split()) for s in segments),
                          segments=len(segments), last_cue_seconds=segments[-1]["start"],
                          caption_sha256=digest(captions), parsed_sha256=digest(parsed),
                          caption_type=source["caption_type"],
                          speaker_attribution=source["speaker_attribution"],
                          human_audio_verified=False)
        elif source["kind"] == "article":
            page = source_dir / "page.html"
            supplied = args.page_files.get(source["id"])
            if supplied:
                if supplied.resolve() != page.resolve():
                    shutil.copyfile(supplied, page)
            elif args.refresh or not page.exists():
                fetch(source["url"], page)
            parser = ArticleParser(source["container_class"])
            parser.feed(page.read_text(encoding="utf-8"))
            body = parser.text()
            if len(body.split()) < source["minimum_words"]:
                raise ValueError("Article container is missing or unexpectedly short")
            text_path = source_dir / "article.txt"
            text_path.write_text(body, encoding="utf-8")
            record.update(status="collected", text_words=len(body.split()),
                          acquisition="imported_page" if supplied else "http_or_cached_page",
                          page_representation=source.get("page_representation", "publisher_html"),
                          page_sha256=digest(page), text_sha256=digest(text_path))
        elif source["kind"] == "podcast":
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
        else:
            raise ValueError("Unsupported source kind: " + source["kind"])
    except Exception as error:
        record.update(status="failed", error=f"{type(error).__name__}: {error}")
    (source_dir / "result.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source", action="append", help="Source ID; repeat to select several")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--transcribe", action="store_true", help="Requires mlx-whisper and a model")
    parser.add_argument("--asr-model", default="mlx-community/whisper-large-v3-turbo")
    parser.add_argument("--caption-file", action="append", default=[], metavar="ID=PATH",
                        help="Register a UTF-8 browser transcript export for a video source")
    parser.add_argument("--page-file", action="append", default=[], metavar="ID=PATH",
                        help="Import a saved publisher article HTML or rendered DOM export")
    args = parser.parse_args()
    manifest = Path(__file__).resolve().parents[1] / "references" / "acquisition-manifest.json"
    sources = json.loads(manifest.read_text(encoding="utf-8"))["sources"]
    known = {source["id"] for source in sources}
    if args.source and set(args.source) - known:
        parser.error("Unknown source IDs: " + ", ".join(sorted(set(args.source) - known)))
    args.caption_files = {}
    for item in args.caption_file:
        source_id, separator, path = item.partition("=")
        if not separator or source_id not in known or not Path(path).is_file():
            parser.error("Expected a known source ID and an existing caption file: " + item)
        if source_id in args.caption_files:
            parser.error("Duplicate caption file for " + source_id)
        args.caption_files[source_id] = Path(path)
    args.page_files = {}
    for item in args.page_file:
        source_id, separator, path = item.partition("=")
        if not separator or source_id not in known or not Path(path).is_file():
            parser.error("Expected a known source ID and an existing page file: " + item)
        if source_id in args.page_files:
            parser.error("Duplicate page file for " + source_id)
        args.page_files[source_id] = Path(path)
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
