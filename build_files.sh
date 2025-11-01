#!/bin/bash

# Build script for Vercel deployment
echo "Installing dependencies..."
pip3.9 install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear