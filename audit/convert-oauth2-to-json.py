#!/data/data/com.termux/files/usr/bin/python
import json
import os
from pathlib import Path

src = Path.home() / ".gam" / "oauth2.txt"
dst = Path.home() / ".gam" / "oauth2.local.json"

raw = src.read_text()
data = json.loads(raw)

tmp = dst.with_suffix(".json.tmp")
tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
os.chmod(tmp, 0o600)
tmp.replace(dst)
os.chmod(dst, 0o600)

print("OK convertido sin imprimir secretos:")
print(dst)
print("bytes:", dst.stat().st_size)
