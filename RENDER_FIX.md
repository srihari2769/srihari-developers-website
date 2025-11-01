# 🚨 RENDER CONFIGURATION FIX

## ⚠️ Important: Update Start Command in Render Dashboard

The current start command in Render is incorrect. Here's how to fix it:

### 1. Go to Your Render Service Dashboard
- Find your `srihari-developers` service
- Go to **Settings** tab
- Scroll down to **Build & Deploy** section

### 2. Update the Start Command
Change from:
```
gunicorn sriharidevelopers.wsgi:application --host 0.0.0.0 --port $PORT
```

To:
```
gunicorn sriharidevelopers.wsgi:application --bind 0.0.0.0:$PORT
```

### 3. Force Redeploy
- Save the settings
- Go to **Manual Deploy** → **Deploy latest commit**
- Or trigger redeploy

## ✅ Correct Render Configuration

### Environment Variables:
```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=*.onrender.com
DATABASE_URL=postgresql://user:password@hostname:port/database
```

### Build Command:
```
./build.sh
```

### Start Command:
```
gunicorn sriharidevelopers.wsgi:application --bind 0.0.0.0:$PORT
```

## 📋 Complete Fix Steps:

1. **Update Start Command** (as shown above)
2. **Add PostgreSQL Database**:
   - Dashboard → "New +" → "PostgreSQL" 
   - Copy Internal Database URL
   - Add as `DATABASE_URL` environment variable
3. **Redeploy**

After this fix, your website will be live! 🚀

## 🎯 Expected Success Message:
```
==> Deploy successful 🎉
==> Your service is live at https://srihari-developers.onrender.com
```