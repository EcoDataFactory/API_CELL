# Stage 008 hardening manifest

branch: local/005-collapse-api-wrapper-layout
head_before_commit: ba398dabe496b84ca39a5af47d907477c59170bf
generated_at_utc: 2026-06-07T18:01:40Z

## Runtime entrypoint

    GAM_py/src/bin/gam

## Runtime path contract

6:SRC="$PY/src"
15:export GAMCFGDIR="$CONFIG"
17:export PYTHONPATH="$SRC/gam:$SRC/vendor:$SRC${PYTHONPATH:+:$PYTHONPATH}"
21:export GAM_CELL_LIVE_SRC="$SRC"
25:export GAM_CELL_CACERTS_PEM="$CACERTS"
30:export TEC_GAM_PY_SRC="$SRC"
35:export TEC_GAM_API_PY="$SRC/gam/gam_api.py"
42:    if [ ! -d "$GAMCFGDIR" ]; then
43:      echo "ERROR: falta GAMCFGDIR=$GAMCFGDIR"
46:    if [ ! -f "$SRC/gam/gam.py" ]; then
47:      echo "ERROR: falta $SRC/gam/gam.py"
51:    exec python "$SRC/gam/gam.py" "$@"
55:    exec python "$SRC/gam/gam_api.py" "$@"
63:        exec python "$SRC/gam/gam_api.py" json keys
69:        exec python "$SRC/gam/gam_api.py" status
84:    echo "GAMCFGDIR=$GAMCFGDIR"
99:    echo "SRC=$SRC"
103:    echo "API=$SRC/gam/gam_api.py"

## Filesystem layout

GAM_py
├── README.md
└── src
    ├── .gitignore
    ├── IMPORT_CONTRACT.md
    ├── atom
    │   ├── __init__.py
    │   ├── auth.py
    │   ├── client.py
    │   ├── core.py
    │   ├── data.py
    │   ├── http.py
    │   ├── http_core.py
    │   ├── http_interface.py
    │   ├── mock_http.py
    │   ├── mock_http_core.py
    │   ├── mock_service.py
    │   ├── service.py
    │   ├── token_store.py
    │   └── url.py
    ├── audit
    │   ├── GAM_py.stage008.sha256
    │   ├── STAGE_007_MANIFEST.md
    │   └── STAGE_008_HARDENING.md
    ├── bin
    │   └── gam
    ├── gam
    │   ├── gam.py
    │   ├── gam_api.py
    │   └── gamlib
    │       ├── __init__.py
    │       ├── glaction.py
    │       ├── glapi.py
    │       ├── glcfg.py
    │       ├── glclargs.py
    │       ├── glentity.py
    │       ├── glgapi.py
    │       ├── glgdata.py
    │       ├── glglobals.py
    │       ├── glindent.py
    │       ├── glmsgs.py
    │       ├── glskus.py
    │       ├── gluprop.py
    │       ├── glverlibs.py
    │       └── yubikey.py
    └── vendor
        ├── gdata
        │   ├── __init__.py
        │   ├── alt
        │   │   ├── __init__.py
        │   │   ├── app_engine.py
        │   │   └── appengine.py
        │   ├── apps
        │   │   ├── __init__.py
        │   │   ├── audit
        │   │   │   ├── __init__.py
        │   │   │   └── service.py
        │   │   ├── contacts
        │   │   │   ├── __init__.py
        │   │   │   └── service.py
        │   │   └── service.py
        │   ├── service.py
        │   └── urlfetch.py
        └── vendor.sh

13 directories, 51 files

## Hash manifest

    GAM_py/src/audit/GAM_py.stage008.sha256

## Validation commands

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/GAM_py/src/gam:$PWD/GAM_py/src/vendor:$PWD/GAM_py/src" python -c "import atom, gdata, gamlib; print(atom.__file__); print(gdata.__file__); print(gamlib.__file__)"
    GAM_py/src/bin/gam status
    GAM_py/src/bin/gam api status
    GAM_py/src/bin/gam live --version

## Security checks

    OK: no sensitive tracked paths
    OK: no bytecode
    OK: no obsolete runtime references
