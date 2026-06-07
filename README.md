# GAM_CELL

Private hardened GAM runtime cell with local PKI separation, audit stages, runtime validation, stable hash verification, and license boundary notes.

## Estado

Repositorio privado para operación controlada de una celda runtime GAM autocontenida.

La celda separa:

- código operativo versionado dentro de `GAM_py/`
- configuración, PKI, runtime y certificados fuera del repositorio
- validaciones runtime mediante comandos del wrapper
- manifiestos de auditoría por etapa
- notas explícitas de límites de licencia

## Comandos principales

    GAM_py/src/bin/gam doctor
    GAM_py/src/bin/gam stage-check
    GAM_py/src/bin/gam release-check
    GAM_py/src/bin/gam final-check

## Estructura

    GAM_CELL/
    ├── GAM_py/
    │   ├── README.md
    │   └── src/
    │       ├── bin/gam
    │       ├── gam/
    │       ├── atom/
    │       ├── vendor/
    │       └── audit/
    ├── LICENSE_NOTES.md
    ├── .env.example
    └── .gitignore

## Validación operativa

Antes de publicar o mover el runtime:

    GAM_py/src/bin/gam final-check

El `final-check` valida:

- árbol Git limpio
- rutas runtime requeridas
- permisos operativos
- `PYTHONPATH`
- imports de `atom`, `gdata` y `gamlib`
- ausencia de bytecode residual
- ausencia de secretos trackeados
- referencias obsoletas operativas
- estado de API
- hash operativo estable

## Hash operativo

El hash operativo estable está en:

    GAM_py/src/audit/GAM_py.runtime.stage014.sha256

Este hash excluye artefactos de auditoría cambiantes y valida los archivos runtime operativos.

## Licencias

Ver:

    LICENSE_NOTES.md

Resumen:

- `GAM_py/src/gam/gam.py`: origen GAM upstream, no relicenciable libremente.
- `GAM_py/src/gam/gamlib/`: origen GAM upstream, no relicenciable libremente.
- `GAM_py/src/atom/`: vendorizado, conservar avisos/licencia original.
- `GAM_py/src/vendor/gdata/`: vendorizado, conservar avisos/licencia original.
- wrapper, auditoría, manifiestos y documentación propia: componentes propios, licenciables aparte sin cambiar obligaciones upstream.

## Seguridad

No subir:

- `.env`
- `.master_env`
- tokens OAuth
- credenciales
- certificados privados
- archivos `.pem`, `.p12`, `.key`, `.crt`, `.cer`
- `conf.json`, `etc.json`, `client_secrets`, `oauth2service`

Validación rápida:

    git ls-files | grep -Ei '(^|/)(\.env|\.master_env)$|oauth|token\.json|secret|private|credential|client_secrets|oauth2service|etc\.json|conf\.json|\.pem$|\.p12$|\.key$|\.crt$|\.cer$' || echo "OK: no sensitive tracked paths"

## Estado publicado

Versión inicial privada:

    v0.1.0-private-runtime
