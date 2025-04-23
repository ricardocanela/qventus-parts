#!/bin/sh

echo "Waiting for the database to be ready..."
sleep 3

echo "Applying migrations..."
python manage.py migrate

echo "Seeding sample data..."
python manage.py shell < src/seed_data.py

echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000
