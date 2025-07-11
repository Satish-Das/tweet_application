# 🐦 Tweet Application

A feature-rich Django-based Twitter-like social media application built with modern web technologies. This application provides a complete social media experience with user authentication, tweet management, social interactions, and a beautiful responsive interface.

## 🚀 Live Demo

Access the application at: `http://127.0.0.1:8000/tweet/`

**Demo Credentials:**
- **Admin**: `admin` / `admin123`
- **Test Users**: `user1`, `user2`, `user3` / `password123`

## ✨ Features Overview

### 🔐 **Authentication & User Management**
- [x] **User Registration**: Complete signup process with email validation
- [x] **User Login/Logout**: Secure authentication system
- [x] **Session Management**: Proper login redirects and session handling
- [x] **User Profile System**: Comprehensive profile management

### 🐦 **Tweet Management**
- [x] **Create Tweets**: Text and photo tweet creation
- [x] **Edit/Delete Tweets**: Full CRUD operations with ownership validation
- [x] **Tweet Timeline**: Chronological tweet display with infinite scroll
- [x] **Tweet Details**: Individual tweet pages with enhanced viewing

### 👥 **Social Features**
- [x] **User Profiles**: Complete profile system with avatars, bio, stats
- [x] **Follow/Unfollow**: Social networking functionality
- [x] **Like System**: Like/unlike tweets with AJAX support and real-time updates
- [x] **Comment System**: Threaded discussions on tweets
- [x] **Search Functionality**: Search for users and tweets with advanced filters

### 🎨 **UI/UX Excellence**
- [x] **Responsive Design**: Mobile-first Bootstrap 5.3.7 interface
- [x] **Modern UI**: Professional styling with custom CSS variables
- [x] **Enhanced Navigation**: Intuitive navbar with user dropdown
- [x] **Interactive Elements**: Smooth animations and transitions
- [x] **Accessibility**: ARIA labels and semantic HTML

### 🔧 **Technical Features**
- [x] **AJAX Integration**: Real-time interactions without page refresh
- [x] **Image Handling**: Photo upload for tweets and profile avatars
- [x] **Database Optimization**: Efficient queries and relationships
- [x] **Error Handling**: Robust error management and user feedback
- [x] **Security**: CSRF protection and secure authentication

## 🏗️ Project Architecture

```
tweet_application/
├── 📄 README.md                    # Project documentation
├── 📄 requirements.txt             # Python dependencies
├── 📁 .venv/                       # Virtual environment
├── 📁 .git/                        # Git repository
└── 📁 tweet_app/                   # Main Django project
    ├── 🗄️ db.sqlite3               # SQLite database
    ├── ⚙️ manage.py                 # Django management script
    ├── 📁 media/                   # User uploaded files
    │   ├── 📁 photos/              # Tweet images
    │   └── 📁 avatars/             # User profile pictures
    ├── 📁 templates/               # Global templates
    │   ├── 🎨 layout.html          # Base template with Bootstrap
    │   ├── 🏠 index.html           # Landing page
    │   └── 📁 registration/        # Authentication templates
    │       ├── 🔐 login.html       # Login page
    │       ├── 📝 register.html    # Registration page
    │       └── 👋 logged_out.html  # Logout confirmation
    ├── 📁 tweet/                   # Main application
    │   ├── 🔧 models.py            # Data models (Tweet, UserProfile, Like, Comment)
    │   ├── 📋 forms.py             # Django forms
    │   ├── 👁️ views.py             # Business logic and controllers
    │   ├── 🌐 urls.py              # URL routing
    │   ├── ⚙️ admin.py             # Admin interface configuration
    │   ├── 📁 templates/           # App-specific templates
    │   │   ├── 📰 tweet_list.html  # Main timeline
    │   │   ├── 📝 tweet_form.html  # Tweet creation/editing
    │   │   ├── 📄 tweet_detail.html # Individual tweet view
    │   │   ├── 👤 profile.html     # User profile page
    │   │   ├── ✏️ profile_edit.html # Profile editing
    │   │   └── 🔍 search.html      # Search results
    │   ├── 📁 migrations/          # Database migrations
    │   └── 📁 templatetags/        # Custom template tags
    └── 📁 tweet_app/               # Django project settings
        ├── ⚙️ settings.py          # Configuration
        ├── 🌐 urls.py              # Main URL configuration
        ├── 🚀 wsgi.py              # WSGI server configuration
        └── 🔄 asgi.py              # ASGI server configuration
```

## 🛠️ Technology Stack

### **Backend Technologies**
- **Framework**: Django 5.2.4 (Python web framework)
- **Database**: SQLite3 (Development) / PostgreSQL (Production ready)
- **Image Processing**: Pillow 11.3.0 (Image handling and manipulation)
- **Authentication**: Django's built-in authentication system
- **ORM**: Django ORM for database interactions

### **Frontend Technologies**
- **CSS Framework**: Bootstrap 5.3.7 (Responsive UI components)
- **Icons**: Font Awesome 6.4.0 (Comprehensive icon library)
- **JavaScript**: Vanilla JS with AJAX for dynamic interactions
- **Templating**: Django Template Language (DTL)

### **Development Tools**
- **Version Control**: Git
- **Package Manager**: pip
- **Environment**: Virtual environment (.venv)
- **Development Server**: Django's built-in server

## 📊 Database Schema

### **Core Models**

#### **Tweet Model**
```python
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Properties
    likes_count = property(lambda self: self.likes.count())
    comments_count = property(lambda self: self.comments.count())
```

#### **UserProfile Model**
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    website = models.URLField(blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### **Like Model**
```python
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES, default='like')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'tweet')
```

#### **Comment Model**
```python
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## 📱 User Interface Features

### **Responsive Design**
- Mobile-first approach with Bootstrap grid system
- Adaptive layouts for desktop, tablet, and mobile
- Touch-friendly interface elements
- Optimized image loading and display

### **Modern UI Components**
- **Navigation**: Collapsible navbar with user dropdown
- **Cards**: Modern card-based layout for tweets
- **Forms**: Styled form controls with validation
- **Buttons**: Consistent button styling with hover effects
- **Modals**: Interactive dialogs for confirmations

### **Interactive Elements**
- **AJAX Likes**: Real-time like/unlike without page refresh
- **Smooth Animations**: CSS transitions and hover effects
- **Dynamic Content**: JavaScript-powered interactions
- **Responsive Images**: Optimized image display

## 🔐 Security Features

### **Authentication & Authorization**
- **CSRF Protection**: Cross-site request forgery protection
- **Session Management**: Secure session handling
- **Password Hashing**: Django's built-in password hashing
- **User Permissions**: Ownership-based access control

### **Data Validation**
- **Form Validation**: Client and server-side validation
- **File Upload Security**: Restricted file types and sizes
- **Input Sanitization**: XSS protection
- **Database Constraints**: Model-level data integrity

## 🌐 API Endpoints

### **Authentication URLs**
- `POST /accounts/login/` - User login
- `POST /accounts/logout/` - User logout
- `GET /accounts/password_change/` - Password change form
- `POST /accounts/password_change/` - Password change submission

### **Tweet URLs**
- `GET /tweet/` - Tweet timeline (home page)
- `GET /tweet/create/` - Tweet creation form
- `POST /tweet/create/` - Tweet creation submission
- `GET /tweet/<int:tweet_id>/` - Tweet detail view
- `GET /tweet/<int:tweet_id>/edit/` - Tweet edit form
- `POST /tweet/<int:tweet_id>/edit/` - Tweet edit submission
- `POST /tweet/<int:tweet_id>/delete/` - Tweet deletion
- `POST /tweet/<int:tweet_id>/like/` - Like/unlike tweet (AJAX)

### **User & Profile URLs**
- `GET /tweet/register/` - User registration form
- `POST /tweet/register/` - User registration submission
- `GET /tweet/profile/` - Current user profile
- `GET /tweet/profile/<str:username>/` - User profile by username
- `GET /tweet/profile/edit/` - Profile edit form
- `POST /tweet/profile/edit/` - Profile edit submission
- `POST /tweet/follow/<str:username>/` - Follow/unfollow user

### **Search URLs**
- `GET /tweet/search/` - Search interface
- `GET /tweet/search/?q=<query>` - Search results

## 🚀 Quick Start Guide

### **Prerequisites**
- Python 3.8+ (Recommended: Python 3.13)
- pip (Python package manager)
- Git (for version control)

### **Installation Steps**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Satish-Das/tweet_application.git
   cd tweet_application
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source .venv/bin/activate
   
   # On Windows:
   .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to Project Directory**
   ```bash
   cd tweet_app
   ```

5. **Setup Database**
   ```bash
   # Run database migrations
   python manage.py migrate
   
   # Create superuser (optional)
   python manage.py createsuperuser
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access Application**
   - **Main App**: http://127.0.0.1:8000/tweet/
   - **Admin Panel**: http://127.0.0.1:8000/admin/
   - **Login**: http://127.0.0.1:8000/accounts/login/

### **Sample Data**
The application includes sample data for testing:
- **Admin User**: `admin` / `admin123`
- **Test Users**: `user1`, `user2`, `user3` / `password123`

## 📦 Dependencies

Current dependencies in `requirements.txt`:
```
asgiref==3.9.1
Django==5.2.4
pillow==11.3.0
sqlparse==0.5.3
```

### **Dependency Details**
- **Django 5.2.4**: Main web framework
- **Pillow 11.3.0**: Image processing library
- **asgiref 3.9.1**: ASGI reference implementation
- **sqlparse 0.5.3**: SQL parsing library

## ⚙️ Configuration

### **Django Settings**
```python
# Key settings in settings.py
DEBUG = True  # Development mode
ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Authentication
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/tweet/'
LOGOUT_REDIRECT_URL = '/tweet/'
```

### **URL Configuration**
```python
# Main URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Media files serving in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 🎨 UI/UX Design

### **Design Philosophy**
- **Modern & Clean**: Minimalist design with focus on content
- **Responsive**: Mobile-first approach with Bootstrap grid
- **User-Friendly**: Intuitive navigation and interactions
- **Professional**: Corporate-ready styling with subtle animations

### **Color Scheme**
```css
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --accent-color: #17a2b8;
    --success-color: #28a745;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    --text-primary: #212529;
    --text-secondary: #6c757d;
    --text-muted: #6c757d;
    --border-color: #dee2e6;
    --light-bg: #f8f9fa;
    --card-bg: #ffffff;
}
```

### **Typography**
- **Font Stack**: System fonts for optimal performance
- **Headings**: Bold, hierarchical typography
- **Body Text**: Readable line height and spacing
- **Icons**: Font Awesome 6.4.0 for consistent iconography

### **Layout Components**
- **Navigation**: Fixed top navbar with user dropdown
- **Content Cards**: Elevated cards with subtle shadows
- **Forms**: Styled form controls with validation feedback
- **Buttons**: Consistent button styles with hover states

## 🔧 Development Tools

### **Code Quality**
- **PEP 8**: Python code styling standards
- **Django Best Practices**: Following Django coding conventions
- **Template Organization**: Logical template structure
- **URL Naming**: Consistent URL naming patterns

### **Development Workflow**
1. **Feature Development**: Create feature branches
2. **Code Review**: Review before merging
3. **Testing**: Unit and integration tests
4. **Migration Management**: Proper database migrations
5. **Documentation**: Update documentation with changes

### **Debugging Tools**
- **Django Debug Toolbar**: Performance and debugging info
- **Django Shell**: Interactive Python shell
- **Django Admin**: Database management interface
- **Browser DevTools**: Frontend debugging

## 📊 Performance Considerations

### **Database Optimization**
- **Efficient Queries**: Using select_related and prefetch_related
- **Database Indexes**: Strategic indexing for performance
- **Query Optimization**: Minimizing database hits
- **Pagination**: Implementing pagination for large datasets

### **Frontend Performance**
- **CDN Usage**: Bootstrap and Font Awesome via CDN
- **Image Optimization**: Proper image sizing and formats
- **Minification**: CSS and JavaScript minification (production)
- **Caching**: Browser caching strategies

### **Security Best Practices**
- **CSRF Protection**: Enabled by default
- **XSS Prevention**: Template auto-escaping
- **SQL Injection**: Using Django ORM
- **File Upload Security**: Restricted file types and sizes

## 🔍 Testing

### **Test Structure**
```python
# Example test case
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tweet

class TweetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_tweet_creation(self):
        tweet = Tweet.objects.create(
            user=self.user,
            text='Test tweet content'
        )
        self.assertEqual(tweet.text, 'Test tweet content')
        self.assertEqual(tweet.user, self.user)
```

### **Running Tests**
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test tweet

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 🚀 Deployment

### **Production Checklist**
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use PostgreSQL or MySQL
- [ ] Set up static file serving
- [ ] Configure email backend
- [ ] Set up logging
- [ ] Use environment variables for secrets
- [ ] Configure SSL/HTTPS
- [ ] Set up monitoring and error tracking

### **Environment Variables**
```bash
# .env file example
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### **Deployment Platforms**
- **Heroku**: Easy deployment with PostgreSQL
- **AWS**: EC2 with RDS and S3
- **DigitalOcean**: Droplets with managed databases
- **Railway**: Modern deployment platform

## 📈 Analytics & Monitoring

### **Key Metrics**
- **User Engagement**: Active users, tweet frequency
- **Content Performance**: Likes, comments, shares
- **System Performance**: Response times, error rates
- **User Growth**: Registration rates, retention

### **Monitoring Tools**
- **Django Admin**: User and content management
- **Database Monitoring**: Query performance
- **Error Tracking**: Sentry or similar services
- **Performance Monitoring**: New Relic or similar

## 🤝 Contributing

### **Development Guidelines**
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Follow coding standards
4. **Test your changes**: Run tests and ensure they pass
5. **Commit your changes**: `git commit -m 'Add some amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**: Describe your changes

### **Code Style**
- **Python**: Follow PEP 8 guidelines
- **Django**: Follow Django best practices
- **HTML/CSS**: Use semantic HTML and consistent styling
- **JavaScript**: Use ES6+ features and consistent formatting

### **Issue Reporting**
- Use GitHub issues for bug reports and feature requests
- Provide detailed descriptions with steps to reproduce
- Include relevant screenshots or error messages
- Label issues appropriately

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

### **Getting Help**
- **Documentation**: Check this README and inline comments
- **Issues**: Create a GitHub issue for bugs or questions
- **Discussions**: Use GitHub discussions for general questions
- **Email**: Contact the maintainer for urgent issues

### **Community**
- **GitHub**: Star the repository and follow for updates
- **Contributing**: Contributions are welcome and appreciated
- **Feedback**: Your feedback helps improve the project

---

## 📋 Development History

### **Version 1.0.0** (July 2025)
- ✅ Initial Django project setup
- ✅ User authentication system
- ✅ Tweet CRUD operations
- ✅ User profile management
- ✅ Follow/unfollow functionality
- ✅ Like system with AJAX
- ✅ Comment system
- ✅ Search functionality
- ✅ Responsive Bootstrap UI
- ✅ Admin interface
- ✅ Error handling and validation

### **Upcoming Features**
- 🔄 Email notifications
- 🔄 Direct messaging
- 🔄 Tweet analytics
- 🔄 Advanced search filters
- 🔄 Real-time updates
- 🔄 Mobile app API

---

**Built with Satish Das using Django and Bootstrap**

*Last updated: July 12, 2025*
