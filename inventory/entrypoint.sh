#!/bin/sh

echo "📁 Asegurando que existe el archivo SQLite..."
touch /app/inventory.db

echo "🔧 Aplicando migraciones..."
alembic upgrade head

echo "🚀 Iniciando servidor..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8001
