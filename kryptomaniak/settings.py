"""
Django settings for kryptomaniak project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

#import psycopg2
from django.conf import settings


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3uku#*7h8r4(hqaya+^j9!u61j_#l2wqj%1fk4ulagyuz!sf@k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
Fonts= os.path.join(STATIC_ROOT,'verdana.ttf')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
	'taggit',
	'kryptomain',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
	
    'taggit_selectize',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'kryptomaniak.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'kryptomaniak.wsgi.application'

import dj_database_url


DATABASES = { 'default': dj_database_url.config() }
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
DATABASES['default'] = dj_database_url.config(default='postgres://zfizmeupreiotb:1240ef586d51e73093f3e908bf9714f0d6f709d1bc09d626d6854973c1eb8711@ec2-54-243-40-26.compute-1.amazonaws.com:5432/dchh5qr1rmicgd')
#DATABASES = {
  # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
     #  'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  # }
 #}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

pdfmetrics.registerFont(TTFont('Verdana',Fonts, 'UTF-8'))
addMapping('Verdana', 0, 0, 'Verdana')

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True
DATE_INPUT_FORMATS = ['%Y-%m-%d']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'

DEFAULT_EMAIL='kryptoapp2@gmail.com'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kryptoapp2@gmail.com'
EMAIL_HOST_PASSWORD = 'zetor1994'
EMAIL_USE_TLS = True




