#!/usr/bin/env python3
import sys
from pathlib import Path

CELL = Path.home() / "GAM_CELL"
MOD = CELL / "GAM_py" / "api-modules"
sys.path.insert(0, str(MOD))

from gam_cell_api import GamCellApi

def main(argv):
    api = GamCellApi()

    cmd = argv[1] if len(argv) > 1 else "help"
    rest = argv[2:]

    if cmd in ("help", "-h", "--help"):
        print("""Uso:
  gam-api-py status
  gam-api-py version
  gam-api-py checkconn
  gam-api-py json keys
  gam-api-py gam <args...>

Descripción:
  API Python interna autosuficiente de GAM_CELL.
  Usa rutas internas de GAM_py y PKI externa.
""")
        return 0

    if cmd == "status":
        api.status()
        return 0

    if cmd == "version":
        return api.version().returncode

    if cmd == "checkconn":
        return api.checkconn().returncode

    if cmd == "json":
        sub = rest[0] if rest else "keys"
        if sub == "keys":
            api.json_keys()
            return 0
        print("Uso: gam-api-py json keys")
        return 2

    if cmd == "gam":
        return api.run_gam(rest).returncode

    print(f"ERROR: comando no reconocido: {cmd}")
    print("Usa: gam-api-py help")
    return 2

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
