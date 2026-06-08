# STAGE 001 - PUBLIC API_CELL DERIVATION

Objective:
Create a clean public API cell branch without GAM runtime files, private PKI, OAuth tokens, credentials, cache, or local runtime state.

Branch:
tec-kio/public-api-cell

Design:
- Minimal API object.
- Local CLI wrapper.
- Route dispatcher.
- Safety policy for sensitive and ephemeral paths.
- Public documentation only.

Excluded:
- GAM upstream runtime.
- GAM vendored dependencies.
- Google Admin Manager runtime.
- GAM_CELL_PKI.
- OAuth files.
- Service account files.
- Certificates.
- Local cache/runtime state.

Initial validation:
- python API_CELL/src/api_cell/app.py health
- python API_CELL/src/api_cell/app.py status
- API_CELL/bin/api-cell health
- git ls-files sensitive scan
