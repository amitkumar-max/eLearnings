

# # # settings.py (Corrected & Render/PostgreSQL Friendly)

# # from pathlib import Path
# # import os
# # from decouple import config
# # import dj_database_url
# # from django.contrib.messages import constants as messages

# # # ----------------------------
# # # Base directory  
# # # ----------------------------
# # BASE_DIR = Path(__file__).resolve().parent.parent

# # # ----------------------------
# # # Security
# # # ----------------------------
# # SECRET_KEY = config("DJANGO_SECRET_KEY", default="django-insecure-default-key")

# # # ----------------------------
# # # Debug mode
# # # ----------------------------
# # DEBUG = config("DEBUG", default=True, cast=bool)

# # # ----------------------------
# # # Allowed hosts
# # # ----------------------------
# # ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")

# # # ----------------------------
# # # CSRF trusted origins
# # # ----------------------------
# # CSRF_TRUSTED_ORIGINS = ['https://elearnings.onrender.com']

# # # ----------------------------
# # # Messages framework
# # # ----------------------------
# # MESSAGE_TAGS = {
# #     messages.DEBUG: 'debug',
# #     messages.INFO: 'info',
# #     messages.SUCCESS: 'success',
# #     messages.WARNING: 'warning',
# #     messages.ERROR: 'error',
# # }

# # # ----------------------------
# # # Installed apps
# # # ----------------------------
# # INSTALLED_APPS = [
# #     'django.contrib.admin',
# #     'django.contrib.auth',
# #     'django.contrib.contenttypes',
# #     'django.contrib.sessions',
# #     'django.contrib.messages',
# #     'django.contrib.staticfiles',

# #     # ✅ Custom Apps
# #     "app.admins",
# #     "app.students",
# #     "app.teachers",
# #     "app.users.apps.UsersConfig",  # ✅ Correct
# # ]

# # # ----------------------------
# # # Auth user model
# # # ----------------------------
# # AUTH_USER_MODEL = "users.CustomUser"

# # # ----------------------------
# # # Middleware
# # # ----------------------------
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

# # # ----------------------------
# # # Root URL configuration
# # # ----------------------------
# # ROOT_URLCONF = 'config.urls'

# # # ----------------------------
# # # Templates
# # # ----------------------------
# # TEMPLATES = [
# #     {
# #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# #         'DIRS': [BASE_DIR / 'templates'],
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

# # # ----------------------------
# # # WSGI application
# # # ----------------------------
# # WSGI_APPLICATION = 'config.wsgi.application'

# # # ----------------------------
# # # Database (Render/PostgreSQL Friendly)
# # # ----------------------------
# # # DATABASES = {
# # #     'default': dj_database_url.config(
# # #         default=config('DATABASE_URL', default=f"postgres://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}:{config('DB_PORT', cast=int)}/{config('DB_NAME')}") + "?sslmode=require"
# # #     )
# # # }

# # # settings.py

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql',
# #         'NAME': 'elearning_db_uk14',  # DB name
# #         'USER': 'elearning_admin',     # DB username
# #         'PASSWORD': 'oHQNTBaEcrlyKkhfP20mKpfq4aVwpu5z',  # DB password
# #         'HOST': 'dpg-d2r3ivl6ubrc73e637d0-a.oregon-postgres.render.com',  # Server address
# #         'PORT': '5432',  # Default PostgreSQL port
# #         'OPTIONS': {
# #             'sslmode': 'require',  # Remote DB ke liye SSL required
# #         },
# #     }
# # }


# # # ----------------------------
# # # Password validation
# # # ----------------------------
# # AUTH_PASSWORD_VALIDATORS = [
# #     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
# #     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# #     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
# #     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# # ]

# # # ----------------------------
# # # Internationalization
# # # ----------------------------
# # LANGUAGE_CODE = 'en-us'
# # TIME_ZONE = 'Asia/Kolkata'
# # USE_I18N = True
# # USE_L10N = True
# # USE_TZ = True

# # # ----------------------------
# # # Static files (CSS, JS, Images)
# # # ----------------------------
# # STATIC_URL = '/static/'
# # STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
# # STATIC_ROOT = BASE_DIR / 'staticfiles'
# # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # # ----------------------------
# # # Media files (uploads)
# # # ----------------------------
# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = BASE_DIR / 'media'

# # # ----------------------------
# # # Default auto field
# # # ----------------------------
# # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# from pathlib import Path
# import os
# from decouple import config
# import dj_database_url
# from django.contrib.messages import constants as messages

# # ----------------------------
# # Base directory
# # ----------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent

# # ----------------------------
# # Security
# # ----------------------------
# SECRET_KEY = config("DJANGO_SECRET_KEY", default="django-insecure-default-key")
# DEBUG = config("DEBUG", default=True, cast=bool)
# ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")
# CSRF_TRUSTED_ORIGINS = ['https://elearnings.onrender.com']

# # ----------------------------
# # Messages framework
# # ----------------------------
# MESSAGE_TAGS = {
#     messages.DEBUG: 'debug',
#     messages.INFO: 'info',
#     messages.SUCCESS: 'success',
#     messages.WARNING: 'warning',
#     messages.ERROR: 'error',
# }

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

#     # Custom Apps
#     "app.admins",
#     "app.students",
#     "app.teachers",
#     "app.users.apps.UsersConfig",
# ]

# # ----------------------------
# # Auth user model
# # ----------------------------
# AUTH_USER_MODEL = "users.CustomUser"

# # ----------------------------
# # Middleware
# # ----------------------------
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# # ----------------------------
# # URL & WSGI
# # ----------------------------
# ROOT_URLCONF = 'config.urls'
# WSGI_APPLICATION = 'config.wsgi.application'

# # ----------------------------
# # Database (Render/PostgreSQL Friendly)
# # ----------------------------
# DATABASES = {
#     'default': dj_database_url.config(
#         default=f"postgres://{config('DB_USER')}:{config('DB_PASSWORD')}@"
#                 f"{config('DB_HOST')}:{config('DB_PORT', cast=int)}/"
#                 f"{config('DB_NAME')}?sslmode=require"
#     )
# }

# # ----------------------------
# # Password validation
# # ----------------------------
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# # ----------------------------
# # Internationalization
# # ----------------------------
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Asia/Kolkata'
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True

# # ----------------------------
# # Static & Media files
# # ----------------------------
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# # ----------------------------
# # Default auto field
# # ----------------------------
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



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

    # Custom apps
    "app.admins",
    "app.students",
    "app.teachers",
    "app.users.apps.UsersConfig",
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
    'default': dj_database_url.config(
        default=f"postgres://{config('DB_USER')}:{config('DB_PASSWORD')}@"
                f"{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}"
                f"?sslmode={config('DB_SSLMODE', default='require')}",
        conn_max_age=600,
        ssl_require=True  # Ensure SSL enforced
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
