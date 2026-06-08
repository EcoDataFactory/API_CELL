#!/data/data/com.termux/files/usr/bin/sh
set -eu

cd "$(dirname "$0")/../.." || exit 1

PYTHONDONTWRITEBYTECODE=1 python API_CELL/src/api_cell/app.py health >/dev/null
PYTHONDONTWRITEBYTECODE=1 python API_CELL/src/api_cell/app.py status >/dev/null
PYTHONDONTWRITEBYTECODE=1 python API_CELL/src/api_cell/app.py get /status >/dev/null
PYTHONDONTWRITEBYTECODE=1 python API_CELL/src/api_cell/app.py post /echo '{"message":"hello"}' >/dev/null
API_CELL/bin/api-cell health >/dev/null

echo "OK: API_CELL smoke test"
