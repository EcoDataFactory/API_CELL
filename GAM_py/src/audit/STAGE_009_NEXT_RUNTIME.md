# Stage 009 next runtime stage manifest

branch: local/009-next-runtime-stage
base_head: 90fa2a835eeabcce6a117658c9ac53e7641873ea
base_tag: stage-008-hardened-runtime-manifest
generated_at_utc: 2026-06-07T18:06:26Z

## Purpose

Stage 009 starts from the hardened Stage 008 runtime.
No layout migration is performed in this checkpoint.

## Active runtime entrypoint

    GAM_py/src/bin/gam

## Runtime contract

    PYTHONPATH="$SRC/gam:$SRC/vendor:$SRC${PYTHONPATH:+:$PYTHONPATH}"

## Current branch

local/009-next-runtime-stage

## Current HEAD

* 90fa2a8 (HEAD -> local/009-next-runtime-stage, tag: stage-008-hardened-runtime-manifest, local/005-collapse-api-wrapper-layout) audit: freeze stage 008 hardened runtime manifest
* f088d46 (tag: stage-007-runtime-import-contract) audit: freeze stage 007 runtime manifest
* 62b3e19 docs: prevent bytecode in import contract validation
* b6a508a docs: document GAM_py runtime import contract
* bbe6671 (tag: stage-006-src-application-layout) chore: remove obsolete local environment ignore rules
* 3528fbb docs: add non-sensitive environment template
* ae518fc chore: remove obsolete CELL_CORE ignore rules
* 7473f88 refactor: promote GAM_py to src application layout

## Active layout

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
        │   └── STAGE_009_NEXT_RUNTIME.md
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

14 directories, 54 files

## Validation commands

    GAM_py/src/bin/gam status
    GAM_py/src/bin/gam api status
    GAM_py/src/bin/gam live --version
