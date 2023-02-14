"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from pathlib import Path
from dotenv import load_dotenv
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Initialise environment variables
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# env('SECRET_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# str(env('DEBUG')) == '1'   .... to get value from .env
DEBUG = os.environ.get('DEBUG') == 'True'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
if not DEBUG:
    ALLOWED_HOSTS += [os.environ.get('ALLOWED_HOSTS')]


# Application definition

INSTALLED_APPS = [
    # Asgi server
    "daphne",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',


    # Async processes for notification
    'channels',

    # rest framework dependencies
    'rest_framework',
    'rest_framework.authtoken',

    # third party apps
    'crispy_forms',
    "crispy_tailwind",
    "debug_toolbar",
    'dj_rest_auth',
    "django_htmx",
    'tailwind',
    'theme',

    # allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    # My apps
    'client',
    'referrals',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, '../FRONTEND/web/templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR, '../FRONTEND/web/static'
]
MEDIA_URL = '/img/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# debug toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Django-allauth settings
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]


SITE_ID = 1


# Django-allauth settings
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_USERNAME_MIN_LENGTH = 5
LOGIN_REDIRECT_URL = '/dashboard'
ACCOUNT_SIGNUP_REDIRECT_URL = '/create_profile'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/create_profile'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGOUT_ON_GET = True
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False
REST_SESSION_LOGIN = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_FORM_CLASS = 'client.forms.SignupForm'


# Django-rest-auth setting
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'core-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'core-refresh-token'

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'client.serializers.CustomSignupSerializer',
}


# Django-rest_framework settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}


# Async config
ASGI_APPLICATION = "core.asgi.application"

# tailwind settings
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# Crispy-form setting
CRISPY_TEMPLATE_PACK = "bootstrap"
