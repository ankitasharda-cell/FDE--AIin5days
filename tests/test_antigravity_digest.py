import io
import json
import os
import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

from scripts import antigravity_digest as digest


class DigestTests(unittest.TestCase):
    def test_feed_filters_old_invalid_and_future_items(self):
        xml = b"""<rss><channel>
          <item><title>Recent</title><link>https://example.com/recent</link>
            <pubDate>Mon, 09 Nov 2026 12:00:00 GMT</pubDate></item>
          <item><title>Old</title><link>https://example.com/old</link>
            <pubDate>Fri, 06 Nov 2026 12:00:00 GMT</pubDate></item>
          <item><title>Future</title><link>https://example.com/future</link>
            <pubDate>Wed, 11 Nov 2026 12:00:00 GMT</pubDate></item>
          <item><title>Bad</title><link>https://example.com/bad</link>
            <pubDate>bad date</pubDate></item>
        </channel></rss>"""
        with patch.object(digest.urllib.request, "urlopen", return_value=io.BytesIO(xml)):
            items = digest.fetch_headlines(datetime(2026, 11, 10, tzinfo=timezone.utc))
        self.assertEqual([item["title"] for item in items], ["Recent"])

    def test_summary_requires_complete_response(self):
        response = {"candidates": [{"finishReason": "MAX_TOKENS", "content": {
            "parts": [{"text": "incomplete"}]}}]}
        with patch.object(digest.urllib.request, "urlopen",
                          return_value=io.BytesIO(json.dumps(response).encode())):
            with self.assertRaises(RuntimeError):
                digest.summarize([{"title": "headline"}], "key")

    def test_smtp_uses_tls_before_login(self):
        connection = MagicMock()
        smtp = connection.__enter__.return_value
        config = {"SMTP_HOST": "smtp.example.com", "SMTP_PORT": "587",
                  "SMTP_USERNAME": "user", "SMTP_PASSWORD": "password",
                  "SMTP_FROM": "sender@example.com", "SMTP_TO": "to@example.com"}
        with patch.object(digest.smtplib, "SMTP", return_value=connection):
            digest.send_email("digest", config)
        self.assertEqual([call[0] for call in smtp.method_calls],
                         ["starttls", "login", "send_message"])

    def test_empty_feed_sends_notice_without_calling_gemini(self):
        env = dict.fromkeys(("GEMINI_API_KEY", "SMTP_HOST", "SMTP_USERNAME",
                             "SMTP_PASSWORD", "SMTP_FROM", "SMTP_TO"), "configured")
        with patch.dict(os.environ, env, clear=True), \
             patch.object(digest, "fetch_headlines", return_value=[]), \
             patch.object(digest, "summarize") as summarize, \
             patch.object(digest, "send_email") as send:
            digest.main()
        summarize.assert_not_called()
        self.assertIn("No matching", send.call_args.args[0])


if __name__ == "__main__":
    unittest.main()
