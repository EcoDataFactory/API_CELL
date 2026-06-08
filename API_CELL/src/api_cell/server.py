from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import sys
from urllib.parse import urlparse

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from api_cell.routes import dispatch


class ApiCellHandler(BaseHTTPRequestHandler):
    server_version = "API_CELL/0.1.0"

    def _read_body(self):
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length <= 0:
            return None

        raw = self.rfile.read(length).decode("utf-8", errors="replace")
        if not raw:
            return None

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return raw

    def _send_response(self, result):
        payload = json.dumps(
            result.to_dict(),
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
        ).encode("utf-8")

        self.send_response(200 if result.ok else 400)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _dispatch(self, method):
        parsed = urlparse(self.path)
        path = parsed.path or "/"
        data = self._read_body()
        result = dispatch(method, path, data)
        self._send_response(result)

    def do_GET(self):
        path = urlparse(self.path).path or "/"
        if path == "/health":
            self._send_response(dispatch("health", path, None))
            return
        if path == "/status":
            self._send_response(dispatch("status", path, None))
            return
        self._dispatch("get")

    def do_POST(self):
        self._dispatch("post")

    def do_PUT(self):
        self._dispatch("put")

    def do_DELETE(self):
        self._dispatch("delete")

    def log_message(self, fmt, *args):
        sys.stderr.write("API_CELL %s - %s\n" % (self.address_string(), fmt % args))


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    host = args[0] if len(args) >= 1 else "127.0.0.1"
    port = int(args[1]) if len(args) >= 2 else 8765

    httpd = HTTPServer((host, port), ApiCellHandler)
    print(f"API_CELL server listening on http://{host}:{port}", flush=True)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("API_CELL server stopping", flush=True)
    finally:
        httpd.server_close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
