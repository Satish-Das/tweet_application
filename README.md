# Tweet Application

A Django-based Twitter-like application built on **July 10-11, 2025**.

## Project Overview

This is a Django web application designed to replicate basic Twitter functionality. The project features a complete tweet system with user authentication, user registration, tweet creation, editing, and deletion capabilities, styled with Bootstrap 5.3.7.

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
    ├── static/                     # Static files directory
    ├── media/                      # Media files directory
    │   └── photos/                 # Tweet photos storage
    ├── templates/                  # Global templates
    │   ├── layout.html             # Base template with Bootstrap
    │   └── registration/           # Authentication templates
    │       ├── login.html          # Login page
    │       ├── register.html       # Registration page
    │       └── logged_out.html     # Logout confirmation
    ├── tweet/                      # Main app directory
    │   ├── __init__.py
    │   ├── admin.py                # Admin interface configuration
    │   ├── apps.py                 # App configuration
    │   ├── models.py               # Tweet model
    │   ├── forms.py                # Tweet and User Registration forms
    │   ├── views.py                # Tweet CRUD + Auth views
    │   ├── urls.py                 # URL routing for tweet app
    │   ├── tests.py                # Test cases
    │   ├── templates/              # App-specific templates
    │   │   ├── index.html          # Home page template
    │   │   ├── tweet_list.html     # Tweet listing page
    │   │   ├── tweet_form.html     # Tweet create/edit form
    │   │   └── tweet_confirm_delete.html # Delete confirmation
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
- [x] **Tweet Model**: Complete with user association, text, photo, timestamps
- [x] **Tweet Forms**: ModelForm for creating and editing tweets
- [x] **User Registration Form**: Custom registration form with email field
- [x] **Tweet Views**: Full CRUD operations (Create, Read, Update, Delete)
- [x] **Authentication Views**: Login, logout, registration functionality
- [x] **URL Routing**: Complete routing for all views
- [x] **Admin Integration**: Tweet model registered in admin panel
- [x] **Bootstrap 5.3.7 Integration**: Modern responsive UI framework
- [x] **Template Structure**: Complete template system with authentication
- [x] **Media Handling**: Photo upload functionality for tweets
- [x] **User Authentication**: Login/logout/registration system
- [x] **Session Management**: Proper login redirects and session handling

### � In Progress
- [ ] User profile management
- [ ] Advanced UI enhancements

### 📋 Pending Features
- [ ] Tweet detail view
- [ ] User profiles
- [ ] Follow/Unfollow functionality
- [ ] Tweet likes and retweets
- [ ] Real-time updates
- [ ] Search functionality

## Technologies Used

- **Backend**: Django 5.2.4
- **Database**: SQLite3
- **Frontend**: Bootstrap 5.3.7 (CDN)
- **Image Processing**: Pillow 11.3.0
- **Python**: Python 3.13
- **Environment**: Virtual environment (.venv)

## Dependencies

Current dependencies as listed in `requirements.txt`:
```
asgiref==3.9.1
Django==5.2.4
pillow==11.3.0
sqlparse==0.5.3
```

## Configuration Details

### Django Settings
- **Debug Mode**: Enabled for development
- **Installed Apps**: Tweet app added to INSTALLED_APPS
- **Templates**: Global templates directory configured
- **Static Files**: Configured with `STATICFILES_DIRS`
- **Media Files**: Configured with `MEDIA_URL` and `MEDIA_ROOT`
- **Database**: SQLite3 (default Django database)
- **Authentication URLs**: Django's built-in auth URLs included
- **Login/Logout Redirects**: Configured to redirect to `/tweet/`

### Tweet Model Features
- **User Association**: Foreign key to Django User model
- **Text Content**: TextField with 240 character limit
- **Photo Upload**: ImageField for tweet images
- **Timestamps**: Auto-generated created_at and updated_at fields
- **String Representation**: User-friendly display format

### URL Configuration
- Admin interface: `/admin/`
- Tweet app: `/tweet/`
- Tweet list: `/tweet/` (homepage)
- Create tweet: `/tweet/create/`
- Edit tweet: `/tweet/<id>/edit/`
- Delete tweet: `/tweet/<id>/delete/`
- User registration: `/tweet/register/`
- Login: `/accounts/login/`
- Logout: `/accounts/logout/`
- Password management: `/accounts/password_change/` etc.
- Static and media files properly routed

### Bootstrap Integration
- **Version**: Bootstrap 5.3.7
- **Theme**: Dark mode enabled (`data-bs-theme="dark"`)
- **CDN**: Using official Bootstrap CDN
- **Components**: Navigation bar, responsive container, utility classes
- **JavaScript**: Bootstrap Bundle with Popper.js included

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
   - Tweet home page: http://127.0.0.1:8000/tweet/
   - Login page: http://127.0.0.1:8000/accounts/login/
   - Registration page: http://127.0.0.1:8000/tweet/register/
   - Admin interface: http://127.0.0.1:8000/admin/

## Bootstrap Configuration

The project uses Bootstrap 5.3.7 for styling and responsive design:

### Bootstrap Features Implemented
- **Responsive Navigation**: Collapsible navbar with dropdown menus
- **Dark Theme**: Enabled by default with `data-bs-theme="dark"`
- **Grid System**: Container-based layout
- **Utility Classes**: Spacing, typography, and color utilities
- **Components**: Navigation, forms, buttons, and cards

### Bootstrap CDN Links Used
```html
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"></script>
```

### Template Structure
- **Base Template**: `templates/layout.html` with Bootstrap framework
- **Authentication Templates**: Login, registration, and logout templates
- **Tweet Templates**: List view, form, and delete confirmation templates
- **Template Inheritance**: All templates extend the base layout
- **Bootstrap Classes**: Used for styling and responsiveness

## Development Notes

- **Date Created**: July 10, 2025
- **Last Updated**: July 11, 2025
- **Framework**: Django 5.2.4
- **UI Framework**: Bootstrap 5.3.7
- **Database**: SQLite3 (development)
- **Image Handling**: Pillow for photo processing

## Models and Forms Implementation

```python
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
```

## Views Implemented

- **index**: Home page view (legacy, redirects to tweet_list)
- **tweet_list**: Display all tweets (connected to URL `/tweet/`)
- **tweet_create**: Create new tweets (connected to URL `/tweet/create/`)
- **tweet_edit**: Edit existing tweets (connected to URL `/tweet/<id>/edit/`)
- **tweet_delete**: Delete tweets (connected to URL `/tweet/<id>/delete/`)
- **register**: User registration (connected to URL `/tweet/register/`)

## Contributing

This project is currently in development. Future contributions will be welcome once the core functionality is implemented.

## License

This project is for educational purposes.