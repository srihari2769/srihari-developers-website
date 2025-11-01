# Render.com Deployment Guide

Your Django website is ready for Render deployment! Follow these steps:

## 🚀 Quick Deploy to Render

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - Srihari Developers website"
git branch -M main
git remote add origin https://github.com/yourusername/srihari-developers.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Use these settings:

**Build Settings:**
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command**: `gunicorn sriharidevelopers.wsgi:application`
- **Python Version**: 3.9

**Environment Variables:**
```
SECRET_KEY=django-insecure-render-production-key-abc123xyz789
DEBUG=False
ALLOWED_HOSTS=*.onrender.com
DATABASE_URL=(will be auto-provided by Render)
```

### Step 3: Add PostgreSQL Database
1. In Render dashboard, click "New +" → "PostgreSQL"
2. Create database
3. Copy the "Internal Database URL"
4. Add it as `DATABASE_URL` environment variable

## ✅ Your Website Will Be Live!

After deployment, your website will be available at:
`https://srihari-developers.onrender.com`

## 🔧 Features Working:
- ✅ Django Admin at `/admin/`
- ✅ Contact Forms with Database Storage
- ✅ Responsive Design
- ✅ Static Files (CSS, JS, Images)
- ✅ PostgreSQL Database
- ✅ SSL Certificate (HTTPS)

## 📱 Admin Access:
Create superuser after deployment:
```bash
# In Render shell
python manage.py createsuperuser
```

**Render is the best choice for Django deployment!** 🎉