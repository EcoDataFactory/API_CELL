GAM_py_json limpio.

Este repo NO debe contener PKI activa ni secretos.

Estructura esperada:
  README.txt
  api-json/
  api-modules/
  api-runtime/
  api-src/
  bin/
  live-src/

PKI externa:
  /data/data/com.termux/files/home/GAM_CELL_PKI/GAM_py_json

Archivos activos externos:
  auth-client/client_secrets.json
  auth-user/oauth2.json
  auth-user/token.json
  auth-service/oauth2service.json
  auth-service/etc.json
  config/gam.cfg
  config/conf.json

Regla OAuth:
  oauth2.txt no se usa como archivo activo.
  El token OAuth usuario activo es auth-user/oauth2.json.
  gam.cfg puede seguir usando la clave oauth2_txt, pero apuntando a auth-user/oauth2.json.
