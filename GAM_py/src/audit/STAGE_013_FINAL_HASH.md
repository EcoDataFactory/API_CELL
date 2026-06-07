# Stage 013 final-check current hash manifest

branch: local/009-next-runtime-stage
base_head: 5f4e3c5039c330577c3e496612d941a7940bb02f
generated_at_utc: 2026-06-07T18:24:47Z

## Purpose

Stage 013 updates final-check to validate the current runtime hash manifest.

## Preferred hash manifest

    GAM_py/src/audit/GAM_py.stage012.sha256

## Fallback hash manifest

    GAM_py/src/audit/GAM_py.stage008.sha256

## Validation

    GAM_py/src/bin/gam final-check

## Current HEAD

* 5f4e3c5 (HEAD -> local/009-next-runtime-stage, tag: stage-012-current-runtime-hash) audit: record stage 012 current runtime hashes
* b12bc15 (tag: stage-011-runtime-final-check) feat: add runtime final-check command
* e0133f2 (tag: stage-010-runtime-release-check) feat: add runtime release-check command
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
