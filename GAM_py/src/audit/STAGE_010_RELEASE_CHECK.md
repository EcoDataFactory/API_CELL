# Stage 010 release-check manifest

branch: local/009-next-runtime-stage
base_head: e932bd6bebb503b5f442ef74dcbc4d8aa77baa86
generated_at_utc: 2026-06-07T18:19:53Z

## Purpose

Stage 010 adds a release-check wrapper command on top of doctor and stage-check.
No layout migration is performed in this checkpoint.

## Runtime commands

    GAM_py/src/bin/gam doctor
    GAM_py/src/bin/gam stage-check
    GAM_py/src/bin/gam release-check

## Expected checks

- clean working tree
- valid runtime paths
- valid permissions
- valid PYTHONPATH
- valid atom, gdata, gamlib imports
- no bytecode
- no sensitive tracked paths
- no obsolete operational references
- API status passes
- audit artifacts exist

## Current layout

.
├── .env.example
├── .gitignore
└── GAM_py
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
        │   ├── STAGE_008_HARDENING.md
        │   ├── STAGE_009_NEXT_RUNTIME.md
        │   └── STAGE_010_RELEASE_CHECK.md
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

14 directories, 55 files
