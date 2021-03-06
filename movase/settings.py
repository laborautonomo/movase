"""
Django settings for movase project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import django.conf.global_settings as DEFAULT_SETTINGS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
LOCAL = True
DEBUG = True
THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]

#Google Analytics: change UA-XXXXX-X to be your site's ID.
GOOGLE_ANALYTICS_CODE = 'UA-XXXXXXXX-XX'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internet Archive client api setting
IA_BOOKMARKS = 'your_user_ia' #ex.: http://archive.org/bookmarks/your_user_ia

try:
    from settings_production import *
except ImportError:
    pass

try:
    from settings_local import *
except ImportError:
    pass


ROOT_URLCONF = 'movase.urls'

WSGI_APPLICATION = 'movase.wsgi.application'

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br' #'en-us'

TIME_ZONE = 'America/Sao_Paulo' #'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'templates/pelican-octopress-theme/static'),
    os.path.join(BASE_DIR, 'movase/static'),
    os.path.join(BASE_DIR, 'ia_client_api/static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/pelican-octopress-theme/templates'),
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'movase/templates'),
)

CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_CONFIGS = {
    'basic_ckeditor': {
        'toolbar': 'Basic',
    },
   'default': {
       'toolbar': 'Full',
       'height': 300,
       'width': '100%',
       'entities_latin': False,
       'allowedContent' : True,
   },
}

THUMBNAIL_ALIASES = {
    '': {
        'large': {'size': (500, 375), 'crop': 'scale'},
        'medium': {'size': (425, 425), 'crop': 'scale'},
        'small': {'size': (140, 140), 'crop': 'scale'},
        
        'gallery-small': {'size': (140, 140), 'crop': 'smart'},
        
        'banner-small': {'size': (140, 90), 'crop': 'scale'},
        
        'segment-small': {'size': (140, 140), 'crop': 'scale'},
    },
}

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.syndication',
    
    'easy_thumbnails',
    'djangosecure',
    'adminsortable',
    'ckeditor',
    
    'carousel',
    'cms',
    'tags',
    'contact',
    'ganalytics',
    'ia_client_api',
    'links',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
)