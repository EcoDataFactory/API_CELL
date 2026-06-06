#!/data/data/com.termux/files/usr/bin/bash
set -u

file="${1:-}"

if [ -z "$file" ]; then
  echo "Uso: $0 archivo.batch"
  exit 2
fi

if [ ! -f "$file" ]; then
  echo "No existe: $file"
  exit 2
fi

echo "### Archivo:"
printf '%s\n' "$file"

echo
echo "### Comandos de ejecución local:"
grep -nEi '^[[:space:]]*execute([[:space:]]|$)' "$file" || echo "Sin execute"

echo
echo "### Comandos destructivos o sensibles:"
grep -nEi '(^|[[:space:]])(delete|purge|trash|transfer|turnoff2sv|signout|deprovision|delegate|forward)([[:space:]]|$)' "$file" || echo "Sin comandos sensibles detectados"
