#!/bin/bash

# Render.com build script for Srihari Developers Django website
set -o errexit  # Exit on error

echo "🏗️  Starting build process for Srihari Developers..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements_sqlite.txt

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Check Python version
echo "🐍 Python version info:"
python --version

# Apply database migrations
echo "🗄️  Applying database migrations..."
# Only run migrations if DATABASE_URL is set
if [ -n "$DATABASE_URL" ]; then
    python manage.py migrate
else
    echo "⚠️  DATABASE_URL not set, skipping migrations for now"
fi

echo "✅ Build completed successfully!"