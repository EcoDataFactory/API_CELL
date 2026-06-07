#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from pathlib import Path

REDACTED_KEYS = {
    "private_key",
    "private_key_id",
    "client_secret",
    "refresh_token",
    "token",
    "id_token",
    "decoded_id_token",
    "token_uri",
    "token_expiry",
    "key_type",
    "access_token",
}

class GamCellApi:
    def __init__(self):
        self.cell = Path(os.environ.get("TEC_GAM_CELL", Path.home() / "GAM_CELL")).resolve()
        self.base = Path(os.environ.get("TEC_GAM_PY_JSON", self.cell / "GAM_py_json")).resolve()
        self.live_src = Path(os.environ.get("TEC_GAM_PY_JSON_SRC", self.base / "live-src")).resolve()
        self.live_config = Path(os.environ.get("TEC_GAM_PY_JSON_CONFIG", Path.home() / "GAM_CELL_PKI" / "GAM_py_json" / "config")).resolve()
        self.api_json = Path(os.environ.get("TEC_GAM_API_JSON", self.base / "api-json")).resolve()
        self.runtime = Path(os.environ.get("TEC_GAM_API_RUNTIME", self.base / "api-runtime")).resolve()
        self.gam_py = self.live_src / "gam.py"

    def env(self):
        e = os.environ.copy()
        e["GAMCFGDIR"] = str(self.live_config)
        e["PYTHONDONTWRITEBYTECODE"] = "1"
        e["TEC_GAM_CELL"] = str(self.cell)
        e["TEC_GAM_PY_JSON"] = str(self.base)
        e["TEC_GAM_PY_JSON_SRC"] = str(self.live_src)
        e["TEC_GAM_PY_JSON_CONFIG"] = str(self.live_config)
        e["TEC_GAM_API_JSON"] = str(self.api_json)
        e["TEC_GAM_API_RUNTIME"] = str(self.runtime)
        return e

    def run_gam(self, args):
        if not self.gam_py.is_file():
            raise SystemExit(f"ERROR: no existe {self.gam_py}")
        if not self.live_config.is_dir():
            raise SystemExit(f"ERROR: no existe GAMCFGDIR {self.live_config}")
        cmd = [sys.executable, str(self.gam_py), *args]
        return subprocess.run(cmd, cwd=str(self.live_src), env=self.env())

    def version(self):
        return self.run_gam(["--version"])

    def checkconn(self):
        return self.run_gam(["checkconn"])

    def json_keys(self):
        for path in sorted(self.api_json.glob("*.json")):
            print(path.name)
            self._print_json_keys(path)

    def _print_json_keys(self, path):
        try:
            data = json.loads(path.read_text())
        except Exception as e:
            print(f"  ERROR: {e}")
            return

        if not isinstance(data, dict):
            print(f"  root: {type(data).__name__}")
            return

        for k, v in data.items():
            lk = str(k).lower()
            if k in REDACTED_KEYS or "token" in lk or "secret" in lk or "private_key" in lk:
                print(f"  {k}: <REDACTED>")
            else:
                print(f"  {k}: {type(v).__name__}")

    def status(self):
        print("GAM_CELL API Python self-contained")
        print(f"cell:        {self.cell}")
        print(f"base:        {self.base}")
        print(f"live_src:    {self.live_src}")
        print(f"live_config: {self.live_config}")
        print(f"api_json:    {self.api_json}")
        print(f"runtime:     {self.runtime}")
        print(f"gam_py:      {self.gam_py}")

        required = [
            self.cell,
            self.base,
            self.live_src,
            self.live_config,
            self.api_json,
            self.runtime,
            self.gam_py,
        ]

        ok = True
        for p in required:
            exists = p.exists()
            print(f"{'OK' if exists else 'FAIL'}: {p}")
            ok = ok and exists

        raise SystemExit(0 if ok else 1)
