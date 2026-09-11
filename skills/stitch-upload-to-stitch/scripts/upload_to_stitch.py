#!/usr/bin/env python3
r"""Upload an image, HTML, or Markdown file to a Stitch project via BatchCreateScreens.

WHY THIS SCRIPT EXISTS:
    The AI model cannot upload files via the MCP tool directly because MCP tool
    call arguments are part of the model's *output*. The model must re-emit the
    entire base64-encoded file as generated text, but its output token limit
    (~16K tokens) is far smaller than a typical file's base64 encoding (e.g.
    a 53KB PNG becomes ~71K chars of base64). The output gets truncated
    mid-string, producing a corrupted payload that the API rejects.

    This script bypasses the model entirely — it reads the file, encodes it
    in-process, and sends the full payload directly over HTTP with no token
    limits.

SUPPORTED FILE TYPES:
    - Images: .png, .jpg, .jpeg, .webp
    - HTML: .html, .htm
    - Markdown: .md

Usage:
    python3 upload_to_stitch.py \
        --project-id <PROJECT_ID> \
        --file-path <PATH_TO_FILE> \
        [--api-url <STITCH_API_BASE_URL>] \
        [--api-key <API_KEY>] \
        [--title <SCREEN_TITLE>] \
        [--generated-by <GENERATED_BY>]

Credentials default to STITCH_API_KEY. The CLI always creates screen instances.
"""

import argparse
import base64
import json
import os
import pathlib
import sys
from typing import Any
import urllib.request
import urllib.parse
import urllib.error

try:
  import ssl
  import certifi
  _SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
except ImportError:
  _SSL_CONTEXT = None


# Maps file extensions to MIME types.
_MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".html": "text/html",
    ".htm": "text/html",
    ".md": "text/markdown",
}


class NoRedirect(urllib.request.HTTPRedirectHandler):
  """Never forward upload credentials or repeat a POST after a redirect."""

  def redirect_request(self, req, fp, code, msg, headers, newurl):
    return None


def secure_urlopen(req, *, timeout=120, context=None):
  """Use verified TLS and disable redirects; no automatic write retries."""
  return urllib.request.build_opener(
      NoRedirect(), urllib.request.HTTPSHandler(context=context)
  ).open(req, timeout=timeout)


def encode_file(path: pathlib.Path) -> str:
  """Read and base64-encode a file."""
  with open(path, "rb") as f:
    return base64.b64encode(f.read()).decode("utf-8")


def call_batch_create_screens(
    api_url: str,
    api_key: str,
    project_id: str,
    requests: list[dict[str, Any]],
    create_screen_instances: bool = False,
    urlopen: Any = secure_urlopen,
) -> dict[str, Any]:
  """Call BatchCreateScreens REST API directly.

  Endpoint: POST /v1/{parent=projects/*}/screens:batchCreate

  Args:
    api_url: Base URL of the Stitch API (e.g. https://stitch.googleapis.com).
    api_key: API key for authentication.
    project_id: The Stitch project ID.
    requests: List of CreateScreenRequest dicts, each containing a screen.
    create_screen_instances: Whether to create screen instances for display.
    urlopen: The urlopen function to use (for testing).

  Returns:
    Parsed JSON response dict.
  """
  endpoint = urllib.parse.urlsplit(api_url)
  if (endpoint.scheme != "https" or not endpoint.hostname or endpoint.username
      or endpoint.password or endpoint.query or endpoint.fragment):
    raise ValueError("上传地址必须为 HTTPS，且不得含凭据、查询参数或片段。")
  if not project_id.isascii() or not project_id.isdigit():
    raise ValueError("缺少有效项目 ID：请从 Stitch 元数据获取纯数字字符串。")
  url = f"{api_url.rstrip('/')}/v1/projects/{project_id}/screens:batchCreate"

  payload = {
      "parent": f"projects/{project_id}",
      "requests": requests,
      "createScreenInstances": create_screen_instances,
  }

  data = json.dumps(payload).encode("utf-8")
  req = urllib.request.Request(
      url,
      data=data,
      headers={
          "Content-Type": "application/json",
          "X-Goog-Api-Key": api_key,
      },
      method="POST",
  )

  try:
    urlopen_kwargs = {"timeout": 120}
    if _SSL_CONTEXT is not None:
      urlopen_kwargs["context"] = _SSL_CONTEXT
    with urlopen(req, **urlopen_kwargs) as resp:
      body = resp.read().decode("utf-8")
      if not body:
        raise ValueError("上传响应为空；先读取项目状态，勿重复提交。")
      return json.loads(body)
  except urllib.error.HTTPError as e:
    raise ValueError(f"上传返回 HTTP {e.code}；请检查授权并读取项目状态，勿重复提交。") from None


def build_screen_request(
    mime_type: str,
    b64_data: str,
    title: str | None = None,
    generated_by: str | None = None,
) -> dict[str, Any]:
  """Build a CreateScreenRequest dict from a file.

  For images, the file is set as the screenshot.
  For HTML, the file is set as the html_code.

  Args:
    mime_type: The MIME type of the file.
    b64_data: Base64-encoded file content.
    title: Optional title for the screen.
    generated_by: Optional value for the generatedBy field (HTML/markdown only).

  Returns:
    A CreateScreenRequest-shaped dict.
  """
  file_obj = {
      "fileContentBase64": b64_data,
      "mimeType": mime_type,
  }

  if mime_type in ("text/html", "text/markdown"):
    screen = {
        "htmlCode": file_obj,
        "screenType": "DOCUMENT",
        "isCreatedByClient": True,
    }
    if not generated_by:
      if mime_type == "text/markdown":
        generated_by = "UserUploadedDesignMd"
      elif mime_type == "text/html":
        generated_by = "UserUploadedHtml"
    if generated_by:
      screen["generatedBy"] = generated_by
  else:
    screen = {
        "screenshot": file_obj,
        "screenType": "IMAGE",
        "isCreatedByClient": True,
    }

  if title:
    screen["title"] = title

  return {"screen": screen}


def parse_args():
  """Parse command-line arguments."""
  parser = argparse.ArgumentParser(
      description="Upload a file to a Stitch project via BatchCreateScreens."
  )
  parser.add_argument("--project-id", required=True, help="Stitch project ID")
  parser.add_argument(
      "--file-path",
      required=True,
      type=pathlib.Path,
      help=(
          "Path to the file to upload. Supported types:"
          f" {', '.join(sorted(_MIME_TYPES.keys()))}"
      ),
  )
  parser.add_argument(
      "--api-url",
      default="https://stitch.googleapis.com",
      help="Stitch API base URL. Defaults to https://stitch.googleapis.com.",
  )
  parser.add_argument(
      "--api-key",
      default=os.environ.get("STITCH_API_KEY"),
      help="Legacy API key flag; prefer STITCH_API_KEY to avoid argv exposure.",
  )
  parser.add_argument(
      "--title",
      default=None,
      help="Optional title for the created screen",
  )
  parser.add_argument(
      "--generated-by",
      default=None,
      help=(
          "Value for the generatedBy field in the screen proto"
          " (HTML/markdown uploads only)."
      ),
  )
  args = parser.parse_args()
  if not args.api_key:
    parser.error("缺少 STITCH_API_KEY：请在运行环境设置，勿粘贴密钥到会话。")
  return args


def main():
  args = parse_args()

  file_path = args.file_path
  file_suffix = file_path.suffix.lower()
  mime_type = _MIME_TYPES.get(file_suffix)

  if mime_type is None:
    print(
        f"Error: Unsupported file type '{file_suffix}'. Supported types:"
        f" {', '.join(sorted(_MIME_TYPES.keys()))}"
    )
    sys.exit(1)

  if not file_path.is_file():
    print(f"Error: File not found: {file_path}")
    sys.exit(1)

  if args.generated_by and mime_type not in ("text/html", "text/markdown"):
    print("Warning: --generated-by is ignored for image uploads.")

  print(f"File:      {file_path}")
  print(f"MIME type: {mime_type}")

  b64_data = encode_file(file_path)
  print(f"Base64:    {len(b64_data)} chars")

  screen_request = build_screen_request(
      mime_type, b64_data, title=args.title, generated_by=args.generated_by,
  )

  print(f"\nUploading to project: {args.project_id}")

  result = call_batch_create_screens(
      api_url=args.api_url,
      api_key=args.api_key,
      project_id=args.project_id,
      requests=[screen_request],
      create_screen_instances=True,
  )

  # Report only the identifiers required by downstream design-system calls.
  summary = {"screens": [{"name": s.get("name")} for s in result.get("screens", [])],
             "screenInstances": [{"id": s.get("id"), "sourceScreen": s.get("sourceScreen")}
                                 for s in result.get("screenInstances", [])]}
  print(json.dumps(summary, indent=2))


if __name__ == "__main__":
  try:
    main()
  except (OSError, ValueError, urllib.error.URLError):
    print("上传未确认完成：请检查输入文件、HTTPS/CA 与授权，再读取项目状态；不要直接重试。", file=sys.stderr)
    sys.exit(1)
