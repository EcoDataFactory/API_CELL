# Stage 007 manifest

branch: local/005-collapse-api-wrapper-layout
head: 62b3e19a46e7b0cf6d3ea03c2da921e5000213c4
tag: stage-007-runtime-import-contract
generated_at_utc: 2026-06-07T17:56:58Z

## Runtime entrypoint

    GAM_py/src/bin/gam

## Active layout

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
    │   └── STAGE_007_MANIFEST.md
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

13 directories, 49 files

## Import contract

# GAM_py runtime import contract

This repository intentionally keeps the legacy GAM import model.

Runtime entrypoint:

    GAM_py/src/bin/gam

The wrapper exports:

    PYTHONPATH="$SRC/gam:$SRC/vendor:$SRC${PYTHONPATH:+:$PYTHONPATH}"

This path order is required:

1. $SRC/gam
   - resolves gamlib
   - contains gam.py
   - contains gam_api.py

2. $SRC/vendor
   - resolves vendored gdata

3. $SRC
   - resolves vendored legacy atom

Current package roots:

    GAM_py/src/
    ├── atom/              # import atom
    ├── gam/
    │   ├── gam.py
    │   ├── gam_api.py
    │   └── gamlib/        # import gamlib
    └── vendor/
        └── gdata/         # import gdata

The following absolute imports are intentional:

    from gamlib import ...
    import atom
    import atom.*
    import gdata
    import gdata.*

Do not rewrite atom or gdata imports unless doing a controlled namespace migration with runtime tests.

Required validation:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/GAM_py/src/gam:$PWD/GAM_py/src/vendor:$PWD/GAM_py/src" python -c "import atom, gdata, gamlib; print(atom.__file__); print(gdata.__file__); print(gamlib.__file__)"

    GAM_py/src/bin/gam status
    GAM_py/src/bin/gam api status
    GAM_py/src/bin/gam live --version

## Runtime smoke tests

    GAM_py/src/bin/gam status
    GAM_py/src/bin/gam api status
    GAM_py/src/bin/gam live --version
