#!/bin/bash

# Render.com build script for Srihari Developers Django website
set -o errexit  # Exit on error

echo "🏗️  Starting build process for Srihari Developers..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Apply database migrations
echo "🗄️  Applying database migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"