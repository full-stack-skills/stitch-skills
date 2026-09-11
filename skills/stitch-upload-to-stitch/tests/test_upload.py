"""Offline upload contract tests; no HTTP request reaches the network."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("upload", Path(__file__).parents[1] / "scripts/upload_to_stitch.py")
upload = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(upload)


class Response(io.BytesIO):
    def getcode(self):
        return 200


class UploadTests(unittest.TestCase):
    def test_key_from_environment(self):
        with patch.dict(os.environ, {"STITCH_API_KEY": "offline-test-key"}), patch("sys.argv", ["upload", "--project-id", "123", "--file-path", "demo.html"]):
            self.assertEqual(upload.parse_args().api_key, "offline-test-key")

    def test_reject_insecure_endpoint_before_transport(self):
        called = []
        with self.assertRaises(ValueError):
            upload.call_batch_create_screens("http://example.invalid", "test", "123", [], urlopen=lambda *a, **k: called.append(a))
        self.assertEqual(called, [])

    def test_request_and_no_payload_logging(self):
        captured = []
        def transport(req, **kwargs):
            captured.append((req, kwargs))
            return Response(json.dumps({"screens": [{"name": "projects/123/screens/a", "privateNote": "PRIVATE_CONTENT"}]}).encode())
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = upload.call_batch_create_screens("https://stitch.googleapis.com", "offline-test-key", "123", [], urlopen=transport)
        self.assertEqual(result["screens"][0]["name"], "projects/123/screens/a")
        self.assertNotIn("PRIVATE_CONTENT", stdout.getvalue())
        self.assertNotIn("offline-test-key", stdout.getvalue())
        self.assertEqual(captured[0][0].method, "POST")
        self.assertEqual(captured[0][1]["timeout"], 120)

    def test_no_cross_origin_redirect(self):
        handler = upload.NoRedirect()
        req = upload.urllib.request.Request("https://stitch.googleapis.com", data=b"{}")
        self.assertIsNone(handler.redirect_request(req, None, 307, "redirect", {}, "https://example.invalid"))

    def test_payload_mappings(self):
        for mime, field in [("image/png", "screenshot"), ("text/html", "htmlCode"), ("text/markdown", "htmlCode")]:
            screen = upload.build_screen_request(mime, "eA==", title="/orders")["screen"]
            self.assertEqual(screen[field]["mimeType"], mime)
            self.assertEqual(screen["title"], "/orders")


if __name__ == "__main__":
    unittest.main()
