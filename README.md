# API_CELL

Public lightweight API cell.

This repository contains a small self-contained API runtime derived from the public architecture of an internal private cell.

It does not include GAM runtime code, Google credentials, OAuth tokens, PKI material, private certificates, service secrets, cache files, or internal runtime state.

## Purpose

API_CELL provides a minimal HTTP-like command surface for local and hosted experiments.

Initial operations:

- GET
- POST
- PUT
- DELETE
- HEALTH
- STATUS

## Boundary

Public repository:

- source code
- simple API object
- route dispatcher
- local CLI wrapper
- safety policy for sensitive and ephemeral paths
- audit notes

Not included:

- private runtime
- private PKI
- OAuth tokens
- Google Admin Manager runtime
- upstream GAM code
- vendored GAM dependencies
- production secrets
- personal device state

## Local commands

Run status:

    python API_CELL/src/api_cell/app.py status

Run health:

    python API_CELL/src/api_cell/app.py health

Run route examples:

    python API_CELL/src/api_cell/app.py get /status
    python API_CELL/src/api_cell/app.py post /echo '{"message":"hello"}'
    python API_CELL/src/api_cell/app.py put /echo '{"message":"updated"}'
    python API_CELL/src/api_cell/app.py delete /echo

Using wrapper:

    API_CELL/bin/api-cell status
    API_CELL/bin/api-cell health
    API_CELL/bin/api-cell get /status

## Security rule

Code inside this public repository must stay clean.

Do not track:

- .env
- .master_env
- token.json
- oauth2.json
- client_secrets.json
- oauth2service.json
- conf.json
- etc.json
- *.pem
- *.p12
- *.key
- *.crt
- *.cer
- __pycache__
- cache
- runtime
- private PKI paths

## Status

Initial public API_CELL derivation.

This branch is intentionally independent from the private runtime tree.
