# -*- coding: utf-8 -*-

"""
Django settings for gilsondev project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', '')
if 'True' == os.environ.get('SEND_MAIL', 'False'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.environ.get('SENDGRID_HOST', 'localhost')
    EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME', '')
    EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD', '')
    EMAIL_PORT = os.environ.get('SENDGRID_PORT', 0)
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*)t@*v7bjhdfjc^=-!renafwhz04-ivi+lk^9pc1(b#-szhp8k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = ['gilsondev.herokuapp.com', 'gilsondev.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

ROOT_URLCONF = 'gilsondev.urls'

WSGI_APPLICATION = 'gilsondev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
