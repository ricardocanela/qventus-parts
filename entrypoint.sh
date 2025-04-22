#!/bin/sh

echo "Aguardando banco de dados ficar pronto..."

# Espera o banco subir
sleep 3

echo "Aplicando migrações..."
python manage.py migrate

echo "Iniciando o servidor..."
python manage.py runserver 0.0.0.0:8000
