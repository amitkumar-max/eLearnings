from pathlib import Path
from decouple import config
import dj_database_url
from django.contrib.messages import constants as messages

# ----------------------------
# Base directory
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Security & Debug
# ----------------------------
SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")
CSRF_TRUSTED_ORIGINS = ['https://elearnings.onrender.com']

# ----------------------------
# Login URL
# ----------------------------
LOGIN_URL = '/users/login/'  # ensures @login_required redirects correctly
# Where to redirect after successful login
LOGIN_REDIRECT_URL = '/students/dashboard/'

# Where to redirect after logout
LOGOUT_REDIRECT_URL = '/users/login/'

# ----------------------------
# Messages framework
# ----------------------------
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

# ----------------------------
# Installed apps
# ----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    # Custom apps
    "app.admins",
    "app.students",
    "app.teachers",
    "app.users.apps.UsersConfig",
    "app.courses",
    'app.exams',   # ✅ Add this line
    'app.payments',
    'app.progress',
    'app.lessons',
    'app.notifications',
    'app.downloads',
    'app.blogs',
    'app.policies',




]

# ----------------------------
# Auth user model
# ----------------------------
AUTH_USER_MODEL = "users.CustomUser"

# ----------------------------
# Middleware
# ----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------
# URL & WSGI
# ----------------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# ----------------------------
# Templates
# ----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ----------------------------
# Database (PostgreSQL via .env + SSL)
# ----------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=(
            f"postgres://{config('DB_USER')}:{config('DB_PASSWORD')}"
            f"@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}"
            f"?sslmode={config('DB_SSLMODE', default='require')}"
        ),
        conn_max_age=600,
        ssl_require=True
    )
}

# ----------------------------
# Password validation
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------------------
# Internationalization
# ----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ----------------------------
# Static & Media files
# ----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ----------------------------
# Default auto field
# ----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
