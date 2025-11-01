# Srihari Developers - Railway Deployment

## Quick Deploy to Railway

### Option 1: GitHub Integration (Recommended)

1. Push this code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit - Srihari Developers website"
git branch -M main
git remote add origin https://github.com/yourusername/srihari-developers.git
git push -u origin main
```

2. Go to [railway.app](https://railway.app)
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will automatically deploy!

### Option 2: Railway CLI (if working)

```bash
railway login
railway init
railway up
```

### Environment Variables to Set in Railway Dashboard:

1. **SECRET_KEY**: `django-insecure-production-key-f8j3k4l9m2n6p7q8r5s1t3u6v9w2x5y8z1a4b7c0d3e6f9`
2. **DEBUG**: `False`
3. **ALLOWED_HOSTS**: `*.railway.app`

### Database:
Railway will automatically provide a PostgreSQL database URL via `DATABASE_URL` environment variable.

### Your website will be live at:
`https://srihari-developers-production.railway.app` (or similar)

## 🎉 Ready for Production!

Your Django + Firebase website is now configured for Railway deployment with:
- ✅ PostgreSQL database integration
- ✅ Static file serving with WhiteNoise  
- ✅ Production-ready settings
- ✅ Environment variable configuration
- ✅ Automatic migrations on deploy