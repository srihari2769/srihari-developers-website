# 🚀 GitHub-Integrated Deployment Guide

## Option 1: Render + GitHub (Recommended)

### Why Render?
- ✅ Direct GitHub integration
- ✅ Automatic deployments on push
- ✅ Free tier for Django apps
- ✅ Built-in PostgreSQL database
- ✅ Easy environment variable management

### Steps:

#### 1. Create GitHub Repository
```bash
# Create new repository on GitHub: srihari-developers-website
# Then connect local repository:
git remote add origin https://github.com/YOUR_USERNAME/srihari-developers-website.git
git branch -M main
git push -u origin main
```

#### 2. Deploy on Render
1. Go to https://dashboard.render.com
2. Sign up/login with GitHub
3. Click "New +" → "Web Service"
4. Select "Build and deploy from a Git repository"
5. Connect to your GitHub repository
6. Configure:
   - **Name**: srihari-developers
   - **Root Directory**: (leave blank)
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn sriharidevelopers.wsgi:application --host 0.0.0.0 --port $PORT`

#### 3. Add Environment Variables
```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=srihari-developers.onrender.com
```

#### 4. Add PostgreSQL Database
1. In Render dashboard: "New +" → "PostgreSQL"
2. Copy the Internal Database URL
3. Add as environment variable: `DATABASE_URL=postgresql://...`

#### 5. Automatic Deployments
- Every time you push to GitHub main branch
- Render automatically rebuilds and deploys
- Zero downtime deployments

---

## Option 2: Heroku + GitHub

### Steps:
1. Create Heroku app
2. Connect to GitHub repository in Heroku dashboard
3. Enable automatic deploys from main branch
4. Add Heroku Postgres addon
5. Configure environment variables

### Files needed:
- `Procfile` (already created)
- `requirements.txt` (already created)
- `runtime.txt` (specify Python version)

---

## Option 3: GitHub Codespaces (Development)

### For development and testing:
1. Enable Codespaces on your repository
2. Create `.devcontainer/devcontainer.json`
3. Configure Python environment
4. Access via web browser

---

## Quick GitHub Setup Commands

```bash
# Initialize git (already done)
git init

# Add all files (already done)
git add .

# Initial commit (already done)
git commit -m "Initial commit - Srihari Developers website"

# Create and connect to GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/srihari-developers-website.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Environment Variables for All Platforms

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
DATABASE_URL=postgresql://username:password@host:port/dbname
ALLOWED_HOSTS=your-domain.com,your-app.onrender.com
FIREBASE_CREDENTIALS={"type":"service_account",...}
```

## Benefits of GitHub Integration

1. **Version Control**: All changes tracked
2. **Automatic Deployments**: Push to deploy
3. **Rollback**: Easy to revert to previous versions  
4. **Collaboration**: Team can contribute
5. **CI/CD**: Automated testing and deployment
6. **Free Hosting**: Most platforms offer free tiers

## Recommended Flow

1. **Push to GitHub** (version control)
2. **Connect to Render** (best for Django)
3. **Configure auto-deploy** (push to deploy)
4. **Add PostgreSQL database** (production data)
5. **Set environment variables** (security)

Your Django app will be live with automatic deployments! 🚀