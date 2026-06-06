#!/data/data/com.termux/files/usr/bin/python
import json
from pathlib import Path

p = Path.home() / ".gam" / "oauth2.txt"

secret_keys = {
    "token",
    "access_token",
    "refresh_token",
    "id_token",
    "id_token_jwt",
    "client_secret",
    "private_key",
    "private_key_id",
}

data = json.loads(p.read_text())

print("file:", p)
print("type:", type(data).__name__)

if isinstance(data, dict):
    print("keys:")
    for k in sorted(data):
        if k in secret_keys:
            print(f"  {k}: <REDACTED>")
        elif k == "scopes":
            scopes = data.get(k) or []
            print(f"  scopes_count: {len(scopes)}")
            for s in scopes:
                print(f"    - {s}")
        else:
            v = data.get(k)
            if isinstance(v, str) and len(v) > 120:
                print(f"  {k}: <string len={len(v)}>")
            else:
                print(f"  {k}: {v}")
