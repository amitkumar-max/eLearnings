



from pathlib import Path
import os
from decouple import config

# ----------------------------
# Base directory  
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Security
# ----------------------------
SECRET_KEY = config("DJANGO_SECRET_KEY", default="django-insecure-default-key")

# ----------------------------
# Debug mode
# ----------------------------
DEBUG = config("DEBUG", default=False, cast=bool)

# ----------------------------
# Allowed hosts
# ----------------------------
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")

# ----------------------------
# CSRF trusted origins
# ----------------------------
CSRF_TRUSTED_ORIGINS = ['https://elearnings.onrender.com']

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
    # 'app.users',
    # 'app.courses',  # ✅ ye hona chahiye exact path ke sath
      # ✅ Custom Apps
    "app.admins",
    # "app.courses",
    # "app.exams",
    # "app.lessons",
    # "app.notifications",
    # "app.payments",
    # "app.progress",
    "app.students",
    "app.teachers",
    "app.users",
    
]
# ✅ settings.py 
AUTH_USER_MODEL = "users.CustomUser"
# user authorised layers ... " 

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
# Root URL configuration
# ----------------------------
ROOT_URLCONF = 'config.urls'

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
# WSGI application
# ----------------------------
WSGI_APPLICATION = 'config.wsgi.application'

# ----------------------------
# Database (PostgreSQL via .env)
# ----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
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
# Static files (CSS, JS, Images)
# ----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ----------------------------
# Media files (uploads)
# ----------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ----------------------------
# Default auto field
# ----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'









































