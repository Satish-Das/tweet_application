# Tweet Application

A Django-based Twitter-like application built on **July 10, 2025**.

## Project Overview

This is a Django web application designed to replicate basic Twitter functionality. The project is currently in its initial setup phase with basic Django structure in place.

## Project Structure

```
tweet_application/
├── README.md
├── requirements.txt
├── .venv/                          # Virtual environment
├── .git/                           # Git repository
└── tweet_app/
    ├── db.sqlite3                  # SQLite database
    ├── manage.py                   # Django management script
    ├── tweet/                      # Main app directory
    │   ├── __init__.py
    │   ├── admin.py                # Admin interface configuration
    │   ├── apps.py                 # App configuration
    │   ├── models.py               # Database models
    │   ├── tests.py                # Test cases
    │   ├── urls.py                 # URL routing for tweet app
    │   ├── views.py                # View functions (index view added)
    │   ├── templates/              # HTML templates directory
    │   │   └── index.html          # Main template with custom styling
    │   ├── migrations/             # Database migrations
    │   │   └── __init__.py
    │   └── __pycache__/            # Python cache files
    └── tweet_app/                  # Project settings directory
        ├── __init__.py
        ├── asgi.py                 # ASGI configuration
        ├── settings.py             # Django settings (tweet app added)
        ├── urls.py                 # Main URL configuration (tweet URLs included)
        ├── wsgi.py                 # WSGI configuration
        └── __pycache__/            # Python cache files
```

## Current Implementation Status

### ✅ Completed Features
- [x] Django project initialization
- [x] Basic project structure setup
- [x] Virtual environment configuration
- [x] Static files configuration
- [x] Media files configuration
- [x] SQLite database setup
- [x] Admin interface setup
- [x] Tweet app integration in settings
- [x] Basic URL routing configuration
- [x] First view function (index view)
- [x] Template directory structure
- [x] Basic HTML template with custom styling

### 🔄 In Progress
- [ ] Tweet models implementation
- [ ] User authentication system
- [ ] Advanced template design
- [ ] Tailwind CSS integration (planned)

### 📋 Pending Features
- [ ] User registration and login
- [ ] Tweet creation and display
- [ ] User profiles
- [ ] Follow/Unfollow functionality
- [ ] Tweet likes and retweets
- [ ] Real-time updates
- [ ] Frontend styling with Tailwind CSS
- [ ] Static files for CSS and JavaScript

## Technologies Used

- **Backend**: Django 5.2.4
- **Database**: SQLite3
- **Python**: Python 3.13
- **Environment**: Virtual environment (.venv)

## Dependencies

Current dependencies as listed in `requirements.txt`:
```
asgiref==3.9.1
Django==5.2.4
sqlparse==0.5.3
```

## Configuration Details

### Django Settings
- **Debug Mode**: Enabled for development
- **Static Files**: Configured with `STATICFILES_DIRS`
- **Media Files**: Configured with `MEDIA_URL` and `MEDIA_ROOT`
- **Database**: SQLite3 (default Django database)
- **Secret Key**: Django-generated secret key for development

### URL Configuration
- Admin interface accessible at `/admin/`
- Tweet app accessible at `/tweet/`
- Main index page at `/tweet/` shows "test template"
- Static and media files properly routed
- URL patterns organized with Django's include() function

## Recent Updates (July 10, 2025)

### New Features Added:
1. **Tweet App Integration**: Added 'tweet' to INSTALLED_APPS in settings.py
2. **URL Routing**: 
   - Created tweet app URLs (`tweet/urls.py`)
   - Integrated tweet URLs into main project URLs
   - Added index view routing
3. **Template System**:
   - Created templates directory structure
   - Added `index.html` template with custom styling
   - Implemented dark theme with black background and white text
4. **View Functions**:
   - Created index view function in `views.py`
   - Connected view to template rendering

### Code Implementation Details:

**views.py**:
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

**tweet/urls.py**:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

**Main URLs Configuration**:
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls'))
]
```

**Template (index.html)**:
- Basic HTML5 structure
- Custom CSS styling with dark theme
- Black background (#000) with white text
- Responsive viewport meta tag
- Test content: "test template"

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd tweet_application
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to project directory**:
   ```bash
   cd tweet_app
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Main application: http://127.0.0.1:8000/
   - Tweet app: http://127.0.0.1:8000/tweet/
   - Admin interface: http://127.0.0.1:8000/admin/

## Tailwind CSS Integration (Planned)

The project is prepared for Tailwind CSS integration. The following commands will be used to configure Tailwind CSS:

### Installation Commands
```bash
# Install Node.js dependencies
npm init -y
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest

# Initialize Tailwind CSS
npx tailwindcss init -p

# Install Django Tailwind (alternative approach)
pip install django-tailwind
```

### Configuration Steps
1. **Add to Django settings**:
   ```python
   INSTALLED_APPS = [
       # ... existing apps
       'tailwind',
       'theme',  # Custom theme app
   ]
   
   TAILWIND_APP_NAME = 'theme'
   ```

2. **Create Tailwind configuration**:
   ```bash
   python manage.py tailwind init
   ```

3. **Install Tailwind CSS**:
   ```bash
   python manage.py tailwind install
   ```

4. **Build Tailwind CSS**:
   ```bash
   python manage.py tailwind build
   ```

5. **Start Tailwind CSS development server**:
   ```bash
   python manage.py tailwind start
   ```

## Development Notes

- **Date Created**: July 10, 2025
- **Framework**: Django 5.2.4
- **Database**: SQLite3 (development)
- **Static Files**: Configured for local development
- **Media Files**: Configured for user uploads
- **Current Status**: Basic template system implemented with custom styling
- **Template Engine**: Django's built-in template system
- **Styling**: Custom CSS (inline) - ready for Tailwind CSS integration

## Next Steps

1. **Integrate Tailwind CSS**: Replace inline CSS with Tailwind utility classes
2. **Implement Tweet Model**: Create database models for tweets, users, and relationships
3. **Add Authentication**: Implement user registration and login system
4. **Enhance Templates**: Create more templates and improve UI/UX
5. **Add JavaScript**: Implement interactive features
6. **Create Static Files Structure**: Organize CSS and JavaScript files
7. **Testing**: Write comprehensive tests for all functionality
8. **Database Migrations**: Create and apply necessary migrations

## Contributing

This project is currently in development. Future contributions will be welcome once the core functionality is implemented.

## License

This project is for educational purposes.