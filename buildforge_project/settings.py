"""
Django settings for buildforge_project project.
Modified for deployment on PythonAnywhere.
"""

from pathlib import Path
import os
# The dotenv library is not needed on PythonAnywhere, but it's harmless to leave it.
# from dotenv import load_dotenv
# load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# CORE DEPLOYMENT SETTINGS
# ==============================================================================

# SECURITY WARNING: keep the secret key used in production secret!
# On PythonAnywhere, you can set this as an Environment Variable on the "Web" tab.
# For now, we'll use the one from your .env file or a default.
SECRET_KEY = os.getenv('SECRET_KEY', 'a-stronger-default-key-for-production')

# SECURITY WARNING: don't run with debug turned on in production!
# This should ALWAYS be False on a live server.
DEBUG = False

# This MUST include your PythonAnywhere domain name.
# Replace 'your-username' with your actual PythonAnywhere username.
ALLOWED_HOSTS = ['BuildForgeBD.pythonanywhere.com']

# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_htmx',
    'users.apps.UsersConfig',
    'catalog.apps.CatalogConfig',
    'builds.apps.BuildsConfig',
    'marketplace.apps.MarketplaceConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise middleware is highly recommended for serving static files efficiently.
    # It should be placed right after SecurityMiddleware.
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'buildforge_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'buildforge_project.wsgi.application'


# ==============================================================================
# DATABASE CONFIGURATION FOR PYTHONANYWHERE
# ==============================================================================
# We will hardcode these values for simplicity on PythonAnywhere.
# Go to your PythonAnywhere "Databases" tab and copy these values exactly.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your-username$buildforge_db',      # e.g., 'ApurbaKumarNath$buildforge_db'
        'USER': 'your-username',                  # e.g., 'ApurbaKumarNath'
        'PASSWORD': 'YOUR_MYSQL_PASSWORD_HERE',     # The password you set on the Databases tab
        'HOST': 'your-username.mysql.pythonanywhere-services.com', # The DB hostname
        'PORT': '3306',
    }
}


# ==============================================================================
# PASSWORDS, INTERNATIONALIZATION, ETC.
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==============================================================================
# STATIC AND MEDIA FILES CONFIGURATION
# ==============================================================================

# The URL to use when referring to static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# The absolute path to the directory where collectstatic will gather static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL that handles media files served from MEDIA_ROOT
MEDIA_URL = '/media/'
# The absolute path to the directory that will hold user-uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# This setting tells WhiteNoise to use a more efficient method to serve compressed files.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ==============================================================================
# CUSTOM APPLICATION SETTINGS
# ==============================================================================

AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
