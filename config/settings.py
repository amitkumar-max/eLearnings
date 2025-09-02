



# # # # # from pathlib import Path
# # # # # import os

# # # # # # Base directory
# # # # # BASE_DIR = Path(__file__).resolve().parent.parent

# # # # # # Security
# # # # # SECRET_KEY = 'django-insecure-your-secret-key'  # apna unique secret key
# # # # # DEBUG = True
# # # # # ALLOWED_HOSTS = []

# # # # # # # Installed apps
# # # # # # INSTALLED_APPS = [
# # # # # #     'django.contrib.admin',
# # # # # #     'django.contrib.auth',
# # # # # #     'django.contrib.contenttypes',
# # # # # #     'django.contrib.sessions',
# # # # # #     'django.contrib.messages',
# # # # # #     'django.contrib.staticfiles',
# # # # # #     'app.users',          # Users module
# # # # # #     'app.courses',        # Courses module
# # # # # #     'app.lessons',        # Lessons module
# # # # # #     'app.exams',          # Exams module
# # # # # #     'app.payments',       # Payments module
# # # # # #     'app.notifications',  # Notifications module
# # # # # #     'app.progress',       # Progress module
# # # # # # ]


# # # # # INSTALLED_APPS = [
# # # # #     'django.contrib.admin',
# # # # #     'django.contrib.auth',
# # # # #     'django.contrib.contenttypes',
# # # # #     'django.contrib.sessions',
# # # # #     'django.contrib.messages',
# # # # #     'django.contrib.staticfiles',
# # # # #     'app.users',  # <- add this instead of 'users'
# # # # # ]




# # # # # # Middleware
# # # # # MIDDLEWARE = [
# # # # #     'django.middleware.security.SecurityMiddleware',
# # # # #     'django.contrib.sessions.middleware.SessionMiddleware',
# # # # #     'django.middleware.common.CommonMiddleware',
# # # # #     'django.middleware.csrf.CsrfViewMiddleware',
# # # # #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# # # # #     'django.contrib.messages.middleware.MessageMiddleware',
# # # # #     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# # # # # ]

# # # # # # URL configuration
# # # # # ROOT_URLCONF = 'config.urls'

# # # # # # Templates
# # # # # TEMPLATES = [
# # # # #     {
# # # # #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# # # # #         'DIRS': [BASE_DIR / "templates"],  # Project-level templates
# # # # #         'APP_DIRS': True,
# # # # #         'OPTIONS': {
# # # # #             'context_processors': [
# # # # #                 'django.template.context_processors.debug',
# # # # #                 'django.template.context_processors.request',
# # # # #                 'django.contrib.auth.context_processors.auth',
# # # # #                 'django.contrib.messages.context_processors.messages',
# # # # #             ],
# # # # #         },
# # # # #     },
# # # # # ]

# # # # # # WSGI application
# # # # # WSGI_APPLICATION = 'config.wsgi.application'

# # # # # # Database
# # # # # DATABASES = {
# # # # #     'default': {
# # # # #         'ENGINE': 'django.db.backends.sqlite3',
# # # # #         'NAME': BASE_DIR / 'db.sqlite3',
# # # # #     }
# # # # # }

# # # # # # Password validation
# # # # # AUTH_PASSWORD_VALIDATORS = [
# # # # #     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
# # # # #     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# # # # # ]

# # # # # # Localization
# # # # # LANGUAGE_CODE = 'en-us'
# # # # # TIME_ZONE = 'Asia/Kolkata'
# # # # # USE_I18N = True
# # # # # USE_TZ = True

# # # # # # Static files
# # # # # STATIC_URL = '/static/'
# # # # # STATICFILES_DIRS = [
# # # # #     BASE_DIR / 'app' / 'static',   # Exact path to static folder in app
# # # # # ]

# # # # # # Media files (user uploads)
# # # # # MEDIA_URL = '/media/'
# # # # # MEDIA_ROOT = BASE_DIR / "media"

# # # # # # Default primary key field type
# # # # # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# # # # from pathlib import Path
# # # # import os
# # # # import dj_database_url  # add this in requirements.txt

# # # # # Base directory
# # # # BASE_DIR = Path(__file__).resolve().parent.parent

# # # # # Security
# # # # SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-your-secret-key')

# # # # DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# # # # # Render ke liye allow hosts me apna domain add karo
# # # # # ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

# # # # ALLOWED_HOSTS = ['elearnings.onrender.com', 'localhost', '127.0.0.1']



# # # # CSRF_TRUSTED_ORIGINS = [
# # # #     'https://*.onrender.com',
# # # # ]

# # # # # Installed apps
# # # # INSTALLED_APPS = [
# # # #     'django.contrib.admin',
# # # #     'django.contrib.auth',
# # # #     'django.contrib.contenttypes',
# # # #     'django.contrib.sessions',
# # # #     'django.contrib.messages',
# # # #     'django.contrib.staticfiles',
# # # #     'app.users',
# # # # ]

# # # # # Middleware
# # # # MIDDLEWARE = [
# # # #     'django.middleware.security.SecurityMiddleware',
# # # #     'whitenoise.middleware.WhiteNoiseMiddleware',  # STATIC files serve karne ke liye (Render)
# # # #     'django.contrib.sessions.middleware.SessionMiddleware',
# # # #     'django.middleware.common.CommonMiddleware',
# # # #     'django.middleware.csrf.CsrfViewMiddleware',
# # # #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# # # #     'django.contrib.messages.middleware.MessageMiddleware',
# # # #     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# # # # ]

# # # # ROOT_URLCONF = 'config.urls'

# # # # TEMPLATES = [
# # # #     {
# # # #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# # # #         'DIRS': [BASE_DIR / "templates"],
# # # #         'APP_DIRS': True,
# # # #         'OPTIONS': {
# # # #             'context_processors': [
# # # #                 'django.template.context_processors.debug',
# # # #                 'django.template.context_processors.request',
# # # #                 'django.contrib.auth.context_processors.auth',
# # # #                 'django.contrib.messages.context_processors.messages',
# # # #             ],
# # # #         },
# # # #     },
# # # # ]

# # # # WSGI_APPLICATION = 'config.wsgi.application'

# # # # # ✅ Database (Render automatically sets DATABASE_URL)
# # # # DATABASES = {
# # # #     'default': dj_database_url.config(
# # # #         default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
# # # #         conn_max_age=600,
# # # #         ssl_require=False
# # # #     )
# # # # }

# # # # AUTH_PASSWORD_VALIDATORS = [
# # # #     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
# # # #     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# # # # ]

# # # # LANGUAGE_CODE = 'en-us'
# # # # TIME_ZONE = 'Asia/Kolkata'
# # # # USE_I18N = True
# # # # USE_TZ = True

# # # # # ✅ Static files
# # # # STATIC_URL = '/static/'
# # # # STATICFILES_DIRS = [
# # # #     BASE_DIR / 'app' / 'static',
# # # # ]
# # # # STATIC_ROOT = BASE_DIR / "staticfiles"
# # # # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # # # MEDIA_URL = '/media/'
# # # # MEDIA_ROOT = BASE_DIR / "media"

# # # # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'






# # # from pathlib import Path
# # # import os
# # # import dj_database_url  # Make sure this is in requirements.txt

# # # # Base directory
# # # BASE_DIR = Path(__file__).resolve().parent.parent

# # # # Security
# # # SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-your-secret-key')

# # # # DEBUG (set True for testing, False for production)
# # # DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# # # # Allowed hosts (add your exact Render domain)
# # # ALLOWED_HOSTS = ['elearnings.onrender.com', 'localhost', '127.0.0.1']

# # # # Trusted origins for CSRF
# # # CSRF_TRUSTED_ORIGINS = [
# # #     'https://elearnings.onrender.com',
# # # ]

# # # # Installed apps
# # # INSTALLED_APPS = [
# # #     'django.contrib.admin',
# # #     'django.contrib.auth',
# # #     'django.contrib.contenttypes',
# # #     'django.contrib.sessions',
# # #     'django.contrib.messages',
# # #     'django.contrib.staticfiles',
# # #     'app.users',  # Your app
# # # ]

# # # # Middleware
# # # MIDDLEWARE = [
# # #     'django.middleware.security.SecurityMiddleware',
# # #     'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files
# # #     'django.contrib.sessions.middleware.SessionMiddleware',
# # #     'django.middleware.common.CommonMiddleware',
# # #     'django.middleware.csrf.CsrfViewMiddleware',
# # #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# # #     'django.contrib.messages.middleware.MessageMiddleware',
# # #     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# # # ]

# # # # Root URL
# # # ROOT_URLCONF = 'config.urls'

# # # # Templates
# # # TEMPLATES = [
# # #     {
# # #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# # #         'DIRS': [BASE_DIR / "templates"],  # Global templates folder
# # #         'APP_DIRS': True,
# # #         'OPTIONS': {
# # #             'context_processors': [
# # #                 'django.template.context_processors.debug',
# # #                 'django.template.context_processors.request',
# # #                 'django.contrib.auth.context_processors.auth',
# # #                 'django.contrib.messages.context_processors.messages',
# # #             ],
# # #         },
# # #     },
# # # ]

# # # # WSGI
# # # WSGI_APPLICATION = 'config.wsgi.application'

# # # # Database (Render automatically provides DATABASE_URL)
# # # DATABASES = {
# # #     'default': dj_database_url.config(
# # #         default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
# # #         conn_max_age=600,
# # #         ssl_require=False
# # #     )
# # # }

# # # # Password validation
# # # AUTH_PASSWORD_VALIDATORS = [
# # #     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
# # #     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# # # ]

# # # # Internationalization
# # # LANGUAGE_CODE = 'en-us'
# # # TIME_ZONE = 'Asia/Kolkata'
# # # USE_I18N = True
# # # USE_TZ = True

# # # # Static files
# # # STATIC_URL = '/static/'
# # # STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']  # Your app static folder
# # # STATIC_ROOT = BASE_DIR / "staticfiles"  # Where collectstatic will copy files
# # # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # # # Media files
# # # MEDIA_URL = '/media/'
# # # MEDIA_ROOT = BASE_DIR / "media"

# # # # Default auto field
# # # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# # # from pathlib import Path
# # # import os
# # # import dj_database_url
# # # from dotenv import load_dotenv

# # # # Load environment variables from .env
# # # # load_dotenv()

# # # load_dotenv(BASE_DIR / '.env')
# # # BASE_DIR = Path(__file__).resolve().parent.parent

# # # # Security
# # # SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key')



# # from pathlib import Path
# # import os
# # import dj_database_url
# # from dotenv import load_dotenv

# # # Base directory
# # BASE_DIR = Path(__file__).resolve().parent.parent

# # # Load environment variables from .env in root
# # load_dotenv(BASE_DIR / '.env')

# # # Security
# # SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key')


# # # Debug
# # DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# # # Allowed hosts
# # ALLOWED_HOSTS = ['elearnings.onrender.com', '127.0.0.1', 'localhost']

# # # Trusted origins
# # CSRF_TRUSTED_ORIGINS = ['https://elearnings.onrender.com']

# # # Installed apps
# # INSTALLED_APPS = [
# #     'django.contrib.admin',
# #     'django.contrib.auth',
# #     'django.contrib.contenttypes',
# #     'django.contrib.sessions',
# #     'django.contrib.messages',
# #     'django.contrib.staticfiles',
# #     'app.users',
# # ]

# # # Middleware
# # MIDDLEWARE = [
# #     'django.middleware.security.SecurityMiddleware',
# #     'whitenoise.middleware.WhiteNoiseMiddleware',
# #     'django.contrib.sessions.middleware.SessionMiddleware',
# #     'django.middleware.common.CommonMiddleware',
# #     'django.middleware.csrf.CsrfViewMiddleware',
# #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# #     'django.contrib.messages.middleware.MessageMiddleware',
# #     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# # ]

# # # Root URL
# # ROOT_URLCONF = 'config.urls'

# # # Templates
# # TEMPLATES = [
# #     {
# #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# #         'DIRS': [BASE_DIR / "templates"],
# #         'APP_DIRS': True,
# #         'OPTIONS': {
# #             'context_processors': [
# #                 'django.template.context_processors.debug',
# #                 'django.template.context_processors.request',
# #                 'django.contrib.auth.context_processors.auth',
# #                 'django.contrib.messages.context_processors.messages',
# #             ],
# #         },
# #     },
# # ]

# # # WSGI
# # WSGI_APPLICATION = 'config.wsgi.application'

# # # Database (PostgreSQL internal URL from .env)
# # DATABASES = {
# #     'default': dj_database_url.config(
# #         default=os.environ.get('DATABASE_URL'),
# #         conn_max_age=600,
# #         ssl_require=True
# #     )
# # }

# # # Password validation
# # AUTH_PASSWORD_VALIDATORS = [
# #     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
# #     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# # ]

# # # Internationalization
# # LANGUAGE_CODE = 'en-us'
# # TIME_ZONE = 'Asia/Kolkata'
# # USE_I18N = True
# # USE_TZ = True

# # # Static files
# # STATIC_URL = '/static/'
# # STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
# # STATIC_ROOT = BASE_DIR / 'staticfiles'
# # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # # Media files
# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = BASE_DIR / 'media'

# # # Default auto field
# # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# from pathlib import Path
# import os
# import dj_database_url
# from dotenv import load_dotenv

# # ----------------------------
# # Base directory
# # ----------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent

# # ----------------------------
# # Load environment variables from .env in project root
# # ----------------------------
# load_dotenv(BASE_DIR / '.env')

# # ----------------------------
# # Security
# # ----------------------------
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key')

# # ----------------------------
# # Debug mode
# # ----------------------------
# DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# # ----------------------------
# # Allowed hosts
# # ----------------------------
# ALLOWED_HOSTS = ['elearnings.onrender.com', '127.0.0.1', 'localhost']

# # ----------------------------
# # Trusted origins
# # ----------------------------
# CSRF_TRUSTED_ORIGINS = ['https://elearnings.onrender.com']

# # ----------------------------
# # Installed apps
# # ----------------------------
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'app.users',
# ]

# # ----------------------------
# # Middleware
# # ----------------------------
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files for production
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# # ----------------------------
# # Root URL configuration
# # ----------------------------
# ROOT_URLCONF = 'config.urls'

# # ----------------------------
# # Templates
# # ----------------------------
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / "templates"],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# # ----------------------------
# # WSGI application
# # ----------------------------
# WSGI_APPLICATION = 'config.wsgi.application'

# # ----------------------------
# # Database (PostgreSQL from .env)
# # ----------------------------
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_URL'),
#         conn_max_age=600,
#         ssl_require=True
#     )
# }

# # ----------------------------
# # Password validation
# # ----------------------------
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# ]

# # ----------------------------
# # Internationalization
# # ----------------------------
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Asia/Kolkata'
# USE_I18N = True
# USE_TZ = True

# # ----------------------------
# # Static files
# # ----------------------------
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # ----------------------------
# # Media files
# # ----------------------------
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# # ----------------------------
# # Default auto field
# # ----------------------------
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# ----------------------------
# Base directory
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Load environment variables from .env
# ----------------------------
load_dotenv(BASE_DIR / '.env')

# ----------------------------
# Security
# ----------------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key')

# ----------------------------
# Debug mode
# ----------------------------
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ----------------------------
# Allowed hosts
# ----------------------------
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

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
    'app.users',   # your custom app
]

# ----------------------------
# Middleware
# ----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files
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
# Database (PostgreSQL)
# ----------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
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
