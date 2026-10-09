"""Guard against promoting mismatched or context-free proxy data as evidence."""

import copy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from collect_sources import collect, parse_proxy_post


POST_ID = '1879206793118658974'
RESPONSE = {
    'code': 200,
    'tweet': {
        'id': POST_ID,
        'author': {'screen_name': 'nikitabier'},
        'created_timestamp': 1736872788,
        'text': 'A substantive public product statement.',
        'media': None,
        'replying_to_status': '123',
    },
}


class ProxyEvidenceTests(unittest.TestCase):
    def parse(self, response):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'response.json'
            path.write_text(json.dumps(response), encoding='utf-8')
            return parse_proxy_post(path, POST_ID)

    def test_valid_response_preserves_context_and_access(self):
        post = self.parse(RESPONSE)
        self.assertEqual(post['replying_to_status'], '123')
        self.assertEqual(post['access'], 'third_party_x_json')
        self.assertEqual(post['date'], '2025-01-14T16:39:48.110000Z')

    def test_wrong_identity_and_unavailable_response_are_rejected(self):
        variants = []
        for field, value in [('id', '1879229105876664666'),
                             ('author', {'screen_name': 'another_author'}),
                             ('created_timestamp', 1736872790)]:
            response = copy.deepcopy(RESPONSE)
            response['tweet'][field] = value
            variants.append(response)
        variants.append({'code': 404, 'tweet': None})
        for response in variants:
            with self.subTest(response=response), self.assertRaises(ValueError):
                self.parse(response)

    def test_empty_and_mentions_only_text_are_not_promoted(self):
        for text in ['', '   ', '@another_author @third_author']:
            response = copy.deepcopy(RESPONSE)
            response['tweet']['text'] = text
            response['tweet']['media'] = {'all': [{'type': 'photo'}]}
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.parse(response)

    def test_cluster_failure_is_not_counted_as_partial_success(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            source_dir = output / 'S99'
            source_dir.mkdir()
            (source_dir / (POST_ID + '.json')).write_text(json.dumps(RESPONSE))
            bad_id = '1879229105876664666'
            (source_dir / (bad_id + '.json')).write_text(json.dumps(RESPONSE))
            source = {'id': 'S99', 'url': 'https://x.com/nikitabier/status/' + POST_ID,
                      'kind': 'x_proxy', 'provider_base_url': 'https://api.fxtwitter.com/status/',
                      'post_ids': [POST_ID, bad_id]}
            result = collect(source, output, SimpleNamespace(refresh=False))
            self.assertEqual(result['status'], 'failed')
            self.assertNotIn('records', result)
            self.assertFalse((source_dir / 'posts.jsonl').exists())


if __name__ == '__main__':
    unittest.main()
