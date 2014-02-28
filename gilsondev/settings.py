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
import bleach

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEFAULT_FROM_EMAIL='contato@gilsondev.com'

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

    'sendgrid',
    'crispy_forms',

    'pages',
    'contact',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
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

# Configurations of django-sendgrid
SENDGRID_EMAIL_HOST = "smtp.sendgrid.net"
SENDGRID_EMAIL_PORT = 587
SENDGRID_EMAIL_USERNAME = os.environ.get('SENDGRID_USERNAME', '')
SENDGRID_EMAIL_PASSWORD = os.environ.get('SENDGRID_PASSWORD', '')

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Bleach
ALLOWED_TAGS = [
    'p',
] + bleach.ALLOWED_TAGS
ALLOWED_ATTRIBUTES = bleach.ALLOWED_ATTRIBUTES.copy()
ALLOWED_ATTRIBUTES.update({
    'a': ['href', 'title', 'rel', 'target'],
})
