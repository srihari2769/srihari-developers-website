# 🏗️ Srihari Developers - Django + Firebase Website

A comprehensive website for Srihari Developers built with Django and Firebase, featuring modern design, responsive layout, and integrated project management.

## 🌟 Features

### Core Functionality
- **Responsive Design**: Mobile-first design with Tailwind CSS
- **Firebase Integration**: Real-time data storage and management
- **Project Showcase**: Dynamic project portfolio with filtering
- **Contact Management**: Lead capture and inquiry handling
- **Admin Panel**: Django admin for content management
- **SEO Optimized**: Meta tags, structured data, and sitemap

### Pages & Sections
- **Homepage**: Hero section, featured projects, services overview, testimonials
- **About**: Company story, mission, vision, team, awards
- **Services**: Detailed service descriptions with inquiry forms
- **Projects**: Portfolio with filtering and project details
- **Contact**: Contact forms, location, FAQ

### Technical Features
- **Django 4.2**: Modern Python web framework
- **Firebase Firestore**: NoSQL database for dynamic content
- **Tailwind CSS**: Utility-first CSS framework
- **AOS Animations**: Scroll-triggered animations
- **Mobile Responsive**: Works perfectly on all devices
- **Form Validation**: Client and server-side validation
- **Error Handling**: Graceful fallbacks and error messages

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Node.js 14+ (for development tools)
- Firebase project (optional, works without Firebase)

### Installation

1. **Clone and Setup**
   ```bash
   git clone <repository-url>
   cd sriharidevelopers
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
   # Create superuser
   python manage.py createsuperuser
   ```

3. **Firebase Configuration (Optional)**
   - Create a Firebase project at https://console.firebase.google.com
   - Enable Firestore Database
   - Generate service account key
   - Download `serviceAccountKey.json`
   - Place it in `firebase_config/` directory
   - Update `FIREBASE_SERVICE_ACCOUNT_KEY` in `settings.py`

4. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://localhost:8000` to view the website.

## 📁 Project Structure

```
sriharidevelopers/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── README.md                   # This file
│
├── sriharidevelopers/          # Main project configuration
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── core/                       # Main application
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── forms.py                # Form classes
│   ├── urls.py                 # URL patterns
│   ├── admin.py                # Admin configuration
│   ├── apps.py                 # App configuration
│   │
│   ├── templates/              # HTML templates
│   │   ├── base.html           # Base template
│   │   ├── home.html           # Homepage
│   │   ├── about.html          # About page
│   │   ├── services.html       # Services page
│   │   ├── projects.html       # Projects page
│   │   └── contact.html        # Contact page
│   │
│   └── static/                 # Static files
│       ├── css/
│       │   └── style.css       # Custom styles
│       ├── js/
│       │   └── main.js         # JavaScript functionality
│       └── images/             # Image assets
│
└── firebase_config/            # Firebase integration
    ├── __init__.py
    ├── firebase_admin_setup.py # Firebase initialization
    ├── utils.py                # Firebase utilities
    └── serviceAccountKey.json.example  # Example config
```

## 🎨 Design System

### Brand Colors
- **Maroon**: `#800000` - Primary brand color
- **Gold**: `#CBA135` - Accent color
- **Cream**: `#FFF8E1` - Background tint
- **Light Gold**: `#F5E6A3` - Hover states

### Typography
- **Headings**: Playfair Display (serif)
- **Body Text**: Poppins (sans-serif)

### Components
- Responsive navigation with mobile menu
- Hero sections with call-to-action buttons
- Card layouts for projects and services
- Modal dialogs for forms
- Toast notifications for feedback

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (optional - defaults to SQLite)
DATABASE_URL=postgresql://user:password@localhost:5432/srihari_db

# Email Configuration (optional)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Firebase (optional)
FIREBASE_PROJECT_ID=your-project-id
```

### Firebase Setup
1. Go to [Firebase Console](https://console.firebase.google.com)
2. Create a new project
3. Enable Firestore Database
4. Go to Project Settings > Service Accounts
5. Generate new private key
6. Download the JSON file as `serviceAccountKey.json`
7. Place in `firebase_config/` directory

### Production Settings
For production deployment:

1. Set `DEBUG=False` in settings
2. Configure `ALLOWED_HOSTS`
3. Use environment variables for secrets
4. Set up proper database (PostgreSQL recommended)
5. Configure static file serving
6. Set up SSL certificates

## 📱 Features in Detail

### Homepage
- Dynamic hero section with company branding
- Featured projects loaded from Firebase/Database
- Services overview with hover effects
- Customer testimonials
- Statistics counters with animations
- Call-to-action sections

### Project Management
- Admin panel for project CRUD operations
- Firebase integration for real-time updates
- Image upload and management
- Project status tracking (Planning, Ongoing, Completed)
- Featured project highlighting
- Category filtering

### Contact System
- Multiple contact forms (general, service inquiry)
- Firebase integration for lead storage
- Form validation and error handling
- Email notifications (configurable)
- Newsletter subscription
- FAQ section with collapsible answers

### Admin Features
- Django admin panel customization
- Project management interface
- Contact inquiry management
- Company information settings
- Testimonial management
- User management

## 🚀 Deployment Options

### 1. Railway (Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### 2. Render
1. Connect your GitHub repository
2. Set environment variables
3. Deploy with automatic builds

### 3. DigitalOcean App Platform
1. Create new app from GitHub
2. Configure build settings
3. Set environment variables
4. Deploy

### 4. Traditional VPS
1. Set up Ubuntu server
2. Install Python, PostgreSQL, Nginx
3. Configure gunicorn and systemd
4. Set up SSL with Let's Encrypt

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test core

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

## 🔧 Development

### Adding New Features
1. Create new views in `core/views.py`
2. Add URL patterns in `core/urls.py`
3. Create templates in `core/templates/`
4. Add static assets as needed
5. Update Firebase utilities if using Firebase

### Customization
- **Colors**: Update CSS variables in `style.css`
- **Fonts**: Change font imports in `base.html`
- **Layout**: Modify templates and Tailwind classes
- **Functionality**: Add JavaScript in `main.js`

### Database Management
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data (if fixtures exist)
python manage.py loaddata sample_data.json
```

## 📋 TODO / Future Enhancements

- [ ] Blog system for construction tips and news
- [ ] Online booking system for consultations
- [ ] Payment integration for bookings
- [ ] Multi-language support (Telugu, English)
- [ ] Progressive Web App (PWA) features
- [ ] Advanced search and filtering
- [ ] Customer dashboard/portal
- [ ] Integration with WhatsApp Business API
- [ ] Google Maps integration for project locations
- [ ] Virtual tours for projects

## 🐛 Troubleshooting

### Common Issues

**Firebase Connection Issues**
- Check `serviceAccountKey.json` path
- Verify Firebase project settings
- Ensure Firestore is enabled

**Static Files Not Loading**
```bash
python manage.py collectstatic
```

**Database Errors**
```bash
# Reset database
python manage.py flush
python manage.py migrate
```

**Import Errors**
- Check virtual environment activation
- Reinstall requirements: `pip install -r requirements.txt`

## 📞 Support

For technical support or questions:
- Email: developer@sriharidevelopers.com
- Phone: +91 99999 99999

## 📄 License

This project is proprietary software developed for Srihari Developers. All rights reserved.

---

**Built with ❤️ for Srihari Developers**