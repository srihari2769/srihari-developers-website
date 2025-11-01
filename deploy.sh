#!/bin/bash

# 🚀 Srihari Developers - Deployment Scripts
# Choose your deployment platform and run the corresponding script

echo "🏗️ Srihari Developers - Django Website Deployment"
echo "=================================================="
echo ""
echo "Choose your deployment platform:"
echo "1) Railway"
echo "2) Render"
echo "3) Vercel"
echo "4) DigitalOcean"
echo "5) Manual VPS Setup"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
  1)
    echo "🚂 Setting up Railway deployment..."
    echo ""
    echo "Prerequisites:"
    echo "- Install Railway CLI: npm install -g @railway/cli"
    echo "- Make sure you're logged in: railway login"
    echo ""
    echo "Commands to run:"
    echo "railway init"
    echo "railway variables set SECRET_KEY='your-secret-key-here'"
    echo "railway variables set DEBUG='False'"
    echo "railway variables set ALLOWED_HOSTS='*.railway.app'"
    echo "railway up"
    ;;
  2)
    echo "🎨 Setting up Render deployment..."
    echo ""
    echo "Steps:"
    echo "1. Connect your GitHub repository to Render"
    echo "2. Choose 'Web Service'"
    echo "3. Set Build Command: pip install -r requirements.txt"
    echo "4. Set Start Command: gunicorn sriharidevelopers.wsgi:application"
    echo "5. Add environment variables in dashboard"
    echo "6. Deploy"
    ;;
  3)
    echo "⚡ Setting up Vercel deployment..."
    echo ""
    echo "Prerequisites:"
    echo "- Install Vercel CLI: npm install -g vercel"
    echo ""
    echo "Commands to run:"
    echo "vercel"
    echo "# Follow the prompts"
    ;;
  4)
    echo "🌊 Setting up DigitalOcean deployment..."
    echo ""
    echo "Steps:"
    echo "1. Create new App in DigitalOcean App Platform"
    echo "2. Connect GitHub repository"
    echo "3. Set Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput"
    echo "4. Set Run Command: gunicorn sriharidevelopers.wsgi:application"
    echo "5. Configure environment variables"
    echo "6. Deploy"
    ;;
  5)
    echo "🖥️ Manual VPS Setup Guide..."
    echo ""
    echo "1. Set up Ubuntu 20.04+ server"
    echo "2. Install dependencies:"
    echo "   sudo apt update"
    echo "   sudo apt install python3-pip python3-dev python3-venv nginx postgresql postgresql-contrib"
    echo ""
    echo "3. Create project directory and clone code"
    echo "4. Set up virtual environment and install requirements"
    echo "5. Configure PostgreSQL database"
    echo "6. Set up Gunicorn service"
    echo "7. Configure Nginx"
    echo "8. Set up SSL with Let's Encrypt"
    echo ""
    echo "For detailed VPS setup, refer to Django deployment documentation."
    ;;
  *)
    echo "❌ Invalid choice. Please run the script again."
    ;;
esac

echo ""
echo "📚 For detailed instructions, check:"
echo "- README.md - Complete documentation"
echo "- SETUP.md - Step-by-step setup guide"
echo ""
echo "🆘 Need help? Contact: support@sriharidevelopers.com"