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

## Local HTTP server

Run local HTTP server:

    python API_CELL/src/api_cell/server.py 127.0.0.1 8765

Then test:

    curl http://127.0.0.1:8765/health
    curl http://127.0.0.1:8765/status
    curl -X POST http://127.0.0.1:8765/echo -H "Content-Type: application/json" --data '{"message":"hello"}'
    curl -X PUT http://127.0.0.1:8765/echo -H "Content-Type: application/json" --data '{"message":"updated"}'
    curl -X DELETE http://127.0.0.1:8765/echo

Stop server with Ctrl-C when running foreground, or kill the saved PID if launched in background.

## Versioned operational commands

The public API_CELL branch includes versioned operational helpers under `API_CELL/bin`.

Start server:

    API_CELL/bin/api-cell-start

Stop server:

    API_CELL/bin/api-cell-stop

Restart server:

    API_CELL/bin/api-cell-restart

Check port state:

    API_CELL/bin/api-cell-port

Narrated state:

    API_CELL/bin/api-cell-narrador

Run all endpoint tests:

    API_CELL/bin/api-cell-test-all

Start, test, and stop in one cycle:

    API_CELL/bin/api-cell-cycle

Run local doctor:

    API_CELL/bin/api-cell-doctor

Default bind:

    127.0.0.1:8765

Override port:

    API_CELL_PORT=9000 API_CELL/bin/api-cell-start

## API_CELL v0.1.3 operational layer

This stage adds a complete versioned operational layer under `API_CELL/bin`.

Main commands:

    API_CELL/bin/api-cell-help
    API_CELL/bin/api-cell-start
    API_CELL/bin/api-cell-stop
    API_CELL/bin/api-cell-restart
    API_CELL/bin/api-cell-status
    API_CELL/bin/api-cell-port
    API_CELL/bin/api-cell-narrador
    API_CELL/bin/api-cell-test-all
    API_CELL/bin/api-cell-cycle
    API_CELL/bin/api-cell-doctor
    API_CELL/bin/api-cell-log
    API_CELL/bin/api-cell-follow-log
    API_CELL/bin/api-cell-open

Recommended full local validation:

    API_CELL/bin/api-cell-cycle

The status endpoint now reports server mode, command mode, public branch flag, and supported methods.

## Endpoint build console

Run a clean endpoint-oriented build:

    API_CELL/bin/api-cell-build

Keep the server open:

    API_CELL/bin/api-cell-run

Follow logs:

    API_CELL/bin/api-cell-tail

Stop the server:

    API_CELL/bin/api-cell-down

The build output reports each endpoint as it is called:

    endpoint called: HEALTH /health
    endpoint called: STATUS /status
    endpoint called: GET /anything
    endpoint called: POST /echo
    endpoint called: PUT /echo
    endpoint called: DELETE /echo

Default bind:

    127.0.0.1:8765
