from __future__ import annotations

import json
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from api_cell.routes import dispatch


def parse_data(raw: str | None):
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)

    if not args:
        print("usage: api-cell METHOD [PATH] [JSON_OR_TEXT_DATA]")
        print("methods: health status get post put delete")
        return 2

    method = args[0]
    path = args[1] if len(args) >= 2 else "/"
    data = parse_data(args[2]) if len(args) >= 3 else None

    result = dispatch(method, path, data)
    print(json.dumps(result.to_dict(), indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
