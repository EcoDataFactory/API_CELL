# Stage 011 final-check manifest

branch: local/009-next-runtime-stage
base_head: e0133f213eafce4721fe149a438eb6d3d3d42454
generated_at_utc: 2026-06-07T18:22:55Z

## Purpose

Stage 011 adds final-check as a top-level operational verification command.

## Runtime commands

    GAM_py/src/bin/gam doctor
    GAM_py/src/bin/gam stage-check
    GAM_py/src/bin/gam release-check
    GAM_py/src/bin/gam final-check

## Current HEAD

* e0133f2 (HEAD -> local/009-next-runtime-stage, tag: stage-010-runtime-release-check) feat: add runtime release-check command
* e932bd6 (tag: stage-009-runtime-stage-check) feat: add runtime stage-check command
* c1104e3 (tag: stage-009-runtime-doctor) feat: add runtime doctor command
* 5877573 (tag: stage-009-next-runtime-stage) audit: open stage 009 runtime branch
* 90fa2a8 (tag: stage-008-hardened-runtime-manifest, local/005-collapse-api-wrapper-layout) audit: freeze stage 008 hardened runtime manifest
* f088d46 (tag: stage-007-runtime-import-contract) audit: freeze stage 007 runtime manifest
* 62b3e19 docs: prevent bytecode in import contract validation
* b6a508a docs: document GAM_py runtime import contract
* bbe6671 (tag: stage-006-src-application-layout) chore: remove obsolete local environment ignore rules
* 3528fbb docs: add non-sensitive environment template
* ae518fc chore: remove obsolete CELL_CORE ignore rules
* 7473f88 refactor: promote GAM_py to src application layout
* becf731 (tag: stage-005-collapse-api-wrapper-layout) docs: record CELL_CORE offrepo retirement
* f0d5caf chore: remove obsolete api wrapper references
* 1e52016 fix: update gam status api path
* 6ae6396 refactor: internalize api wrapper under gam core

## Layout

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
        │   ├── STAGE_010_RELEASE_CHECK.md
        │   └── STAGE_011_FINAL_CHECK.md
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

14 directories, 56 files
