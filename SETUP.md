# 🚀 Setup Guide - Srihari Developers Website

This guide will help you set up the Srihari Developers website locally and deploy it to production.

## 📋 Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher installed
- Git installed
- A text editor (VS Code recommended)
- Firebase account (optional, for full functionality)

## 🛠️ Local Development Setup

### Step 1: Clone and Navigate
```bash
# Clone the repository
git clone <your-repository-url>
cd thefinalwar

# Or if starting fresh, you already have the files
cd c:\Users\psrih\Documents\thefinalwar
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows PowerShell/Command Prompt:
venv\Scripts\activate

# Git Bash on Windows:
source venv/Scripts/activate

# macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```bash
# Create database tables
python manage.py makemigrations core
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

### Step 5: Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see your website!

## 🔥 Firebase Configuration (Optional)

Firebase enables real-time data storage and enhanced functionality.

### Step 1: Create Firebase Project
1. Go to [Firebase Console](https://console.firebase.google.com)
2. Click "Create a project"
3. Enter project name: `srihari-developers`
4. Enable Google Analytics (optional)
5. Create project

### Step 2: Enable Firestore
1. In Firebase console, go to "Firestore Database"
2. Click "Create database"
3. Choose "Start in test mode"
4. Select your preferred location
5. Click "Done"

### Step 3: Generate Service Account Key
1. Go to Project Settings (gear icon)
2. Click "Service accounts" tab
3. Click "Generate new private key"
4. Download the JSON file
5. Rename it to `serviceAccountKey.json`
6. Place it in the `firebase_config/` directory

### Step 4: Update Django Settings
The settings are already configured to look for `firebase_config/serviceAccountKey.json`.

Your Firebase integration is now ready!

## 🌐 Environment Variables

Create a `.env` file in your project root for sensitive configuration:

```env
# Django Configuration
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app

# Database (optional - uses SQLite by default)
DATABASE_URL=postgresql://username:password@localhost:5432/srihari_db

# Email Configuration (optional)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Firebase (optional - auto-detected if serviceAccountKey.json exists)
FIREBASE_PROJECT_ID=your-firebase-project-id
```

## 📱 Testing the Website

### Test Basic Functionality
1. **Homepage**: Check hero section, services overview
2. **About Page**: Verify company information loads
3. **Services**: Test service inquiry forms
4. **Projects**: Check project display and filtering
5. **Contact**: Test contact form submission
6. **Admin Panel**: Visit `/admin` and log in

### Test Firebase Integration (if configured)
1. Submit a contact form
2. Check Firebase console for new data
3. Add a project through admin panel
4. Verify it appears on the projects page

## 🚀 Production Deployment

### Option 1: Railway (Easiest)

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and Initialize**
   ```bash
   railway login
   railway init
   ```

3. **Set Environment Variables**
   ```bash
   railway variables set SECRET_KEY="your-secret-key"
   railway variables set DEBUG="False"
   railway variables set ALLOWED_HOSTS="*.railway.app"
   ```

4. **Deploy**
   ```bash
   railway up
   ```

### Option 2: Render

1. Connect your GitHub repository to Render
2. Choose "Web Service"
3. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn sriharidevelopers.wsgi:application`
4. Add environment variables in Render dashboard
5. Deploy

### Option 3: Vercel (for static sites)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Configure for Django**
   ```bash
   vercel
   ```

3. **Follow prompts and deploy**

### Option 4: DigitalOcean App Platform

1. Connect GitHub repository
2. Configure build settings:
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Run Command: `gunicorn sriharidevelopers.wsgi:application`
3. Set environment variables
4. Deploy

## 🔧 Production Checklist

Before going live, ensure:

- [ ] `DEBUG=False` in production
- [ ] Proper `SECRET_KEY` set
- [ ] `ALLOWED_HOSTS` configured
- [ ] Database configured (PostgreSQL recommended)
- [ ] Static files serving configured
- [ ] Firebase service account key uploaded securely
- [ ] Email settings configured
- [ ] SSL certificate enabled
- [ ] Domain name pointed to deployment

## 📊 Adding Sample Data

### Through Django Admin
1. Visit `/admin`
2. Log in with superuser credentials
3. Add Projects, Company Info, Testimonials

### Through Firebase Console (if using Firebase)
1. Open Firebase console
2. Go to Firestore Database
3. Create collections: `projects`, `contacts`, `testimonials`
4. Add sample documents

### Sample Project Data
```json
{
  "title": "Luxury Villa Construction",
  "description": "Modern 3BHK villa with premium finishes",
  "category": "residential",
  "status": "completed",
  "featured": true,
  "image_url": "https://example.com/villa.jpg",
  "location": "Hyderabad",
  "completion_date": "2023-12-01",
  "client_name": "Mr. Rajesh Kumar"
}
```

## 🎨 Customization Guide

### Changing Brand Colors
Edit `core/static/css/style.css`:
```css
:root {
  --color-maroon: #800000;      /* Your primary color */
  --color-gold: #CBA135;        /* Your accent color */
  --color-cream: #FFF8E1;       /* Your light background */
  --color-light-gold: #F5E6A3;  /* Your hover color */
}
```

### Adding New Pages
1. Create view in `core/views.py`
2. Add URL pattern in `core/urls.py`
3. Create template in `core/templates/`
4. Add navigation link in `base.html`

### Modifying Forms
1. Edit form classes in `core/forms.py`
2. Update templates to include new fields
3. Modify view functions to handle new data
4. Update Firebase services if needed

## 🐛 Troubleshooting

### Common Issues

**"No module named 'django'"**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

**Firebase connection errors**
- Check `serviceAccountKey.json` path
- Verify Firebase project settings
- Ensure internet connection

**Static files not loading in production**
- Run `python manage.py collectstatic`
- Configure web server to serve static files
- Check `STATIC_ROOT` and `STATIC_URL` settings

**Database errors**
- Run `python manage.py migrate`
- Check database connection settings
- Ensure database service is running

**Port already in use**
```bash
# Use different port
python manage.py runserver 8080

# Or find and kill process using port 8000
netstat -ano | findstr :8000
taskkill /PID <process_id> /F
```

### Getting Help

If you encounter issues:
1. Check the Django logs for error messages
2. Verify all environment variables are set correctly
3. Ensure all dependencies are installed
4. Check Firebase console for authentication issues

## 📞 Support

For additional support:
- Email: support@sriharidevelopers.com
- Phone: +91 99999 99999
- Documentation: Check README.md for detailed information

## 🎉 Success!

Once everything is set up correctly, you should have:
- A fully functional construction company website
- Real-time project management with Firebase
- Contact form integration
- Responsive design across all devices
- Admin panel for content management
- Production-ready deployment

**Congratulations! Your Srihari Developers website is now ready! 🚀**