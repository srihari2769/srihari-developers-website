# 🚀 Srihari Developers - Deployment Scripts (Windows)
# Choose your deployment platform and run the corresponding commands

Write-Host "🏗️ Srihari Developers - Django Website Deployment" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Choose your deployment platform:" -ForegroundColor Yellow
Write-Host "1) Railway" -ForegroundColor White
Write-Host "2) Render" -ForegroundColor White
Write-Host "3) Vercel" -ForegroundColor White
Write-Host "4) DigitalOcean" -ForegroundColor White
Write-Host "5) Manual VPS Setup" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter your choice (1-5)"

switch ($choice) {
    1 {
        Write-Host "🚂 Setting up Railway deployment..." -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Prerequisites:" -ForegroundColor Yellow
        Write-Host "- Install Node.js from https://nodejs.org"
        Write-Host "- Install Railway CLI: npm install -g @railway/cli"
        Write-Host "- Make sure you're logged in: railway login"
        Write-Host ""
        Write-Host "Commands to run:" -ForegroundColor Green
        Write-Host "railway init"
        Write-Host "railway variables set SECRET_KEY='your-secret-key-here'"
        Write-Host "railway variables set DEBUG='False'"
        Write-Host "railway variables set ALLOWED_HOSTS='*.railway.app'"
        Write-Host "railway up"
    }
    2 {
        Write-Host "🎨 Setting up Render deployment..." -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Steps:" -ForegroundColor Yellow
        Write-Host "1. Go to https://render.com and sign up/login"
        Write-Host "2. Connect your GitHub repository"
        Write-Host "3. Choose 'Web Service'"
        Write-Host "4. Set Build Command: pip install -r requirements.txt"
        Write-Host "5. Set Start Command: gunicorn sriharidevelopers.wsgi:application"
        Write-Host "6. Add environment variables in dashboard:"
        Write-Host "   - SECRET_KEY: your-secret-key"
        Write-Host "   - DEBUG: False"
        Write-Host "   - ALLOWED_HOSTS: *.onrender.com"
        Write-Host "7. Click Deploy"
    }
    3 {
        Write-Host "⚡ Setting up Vercel deployment..." -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Prerequisites:" -ForegroundColor Yellow
        Write-Host "- Install Node.js from https://nodejs.org"
        Write-Host "- Install Vercel CLI: npm install -g vercel"
        Write-Host ""
        Write-Host "Commands to run:" -ForegroundColor Green
        Write-Host "vercel login"
        Write-Host "vercel"
        Write-Host "# Follow the prompts to deploy"
    }
    4 {
        Write-Host "🌊 Setting up DigitalOcean deployment..." -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Steps:" -ForegroundColor Yellow
        Write-Host "1. Go to https://cloud.digitalocean.com"
        Write-Host "2. Create new App in App Platform"
        Write-Host "3. Connect GitHub repository"
        Write-Host "4. Configure build settings:"
        Write-Host "   - Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput"
        Write-Host "   - Run Command: gunicorn sriharidevelopers.wsgi:application"
        Write-Host "5. Set environment variables:"
        Write-Host "   - SECRET_KEY: your-secret-key"
        Write-Host "   - DEBUG: False"
        Write-Host "   - ALLOWED_HOSTS: *.ondigitalocean.app"
        Write-Host "6. Deploy"
    }
    5 {
        Write-Host "🖥️ Manual VPS Setup Guide..." -ForegroundColor Cyan
        Write-Host ""
        Write-Host "For Windows Server:" -ForegroundColor Yellow
        Write-Host "1. Set up Windows Server 2019/2022"
        Write-Host "2. Install Python 3.8+ from python.org"
        Write-Host "3. Install IIS with CGI module"
        Write-Host "4. Clone your repository"
        Write-Host "5. Set up virtual environment"
        Write-Host "6. Install requirements"
        Write-Host "7. Configure IIS to serve Django app"
        Write-Host ""
        Write-Host "For Linux VPS:" -ForegroundColor Yellow
        Write-Host "1. Use Ubuntu 20.04+ or CentOS 8+"
        Write-Host "2. Install Python, Nginx, PostgreSQL"
        Write-Host "3. Set up Gunicorn service"
        Write-Host "4. Configure Nginx reverse proxy"
        Write-Host "5. Set up SSL certificates"
        Write-Host ""
        Write-Host "For detailed VPS setup, refer to Django deployment documentation."
    }
    default {
        Write-Host "❌ Invalid choice. Please run the script again." -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "📚 For detailed instructions, check:" -ForegroundColor Yellow
Write-Host "- README.md - Complete documentation"
Write-Host "- SETUP.md - Step-by-step setup guide"
Write-Host ""
Write-Host "🔥 Firebase Setup:" -ForegroundColor Yellow
Write-Host "1. Go to https://console.firebase.google.com"
Write-Host "2. Create new project"
Write-Host "3. Enable Firestore Database"
Write-Host "4. Generate service account key"
Write-Host "5. Download and place in firebase_config/serviceAccountKey.json"
Write-Host ""
Write-Host "🆘 Need help? Contact: support@sriharidevelopers.com" -ForegroundColor Green

# Pause to keep window open
Read-Host "Press Enter to exit"