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
    │   ├── views.py                # View functions
    │   └── migrations/             # Database migrations
    │       └── __init__.py
    └── tweet_app/                  # Project settings directory
        ├── __init__.py
        ├── asgi.py                 # ASGI configuration
        ├── settings.py             # Django settings
        ├── urls.py                 # Main URL configuration
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

### 🔄 In Progress
- [ ] Tweet models implementation
- [ ] User authentication system
- [ ] Tweet views and templates
- [ ] Tailwind CSS integration

### 📋 Pending Features
- [ ] User registration and login
- [ ] Tweet creation and display
- [ ] User profiles
- [ ] Follow/Unfollow functionality
- [ ] Tweet likes and retweets
- [ ] Real-time updates
- [ ] Frontend styling with Tailwind CSS

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
- Static and media files properly routed
- Ready for additional URL patterns

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

## Next Steps

1. **Implement Tweet Model**: Create database models for tweets, users, and relationships
2. **Add Authentication**: Implement user registration and login system
3. **Create Templates**: Design HTML templates for tweet display
4. **Integrate Tailwind CSS**: Add modern styling to the application
5. **Add JavaScript**: Implement interactive features
6. **Testing**: Write comprehensive tests for all functionality

## Contributing

This project is currently in development. Future contributions will be welcome once the core functionality is implemented.

## License

This project is for educational purposes.