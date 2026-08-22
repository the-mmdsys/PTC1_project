# Django settings for development environment

from .base import *

SECRET_KEY = 'django-insecure-=s6u!8j#kwvaxev9z&4z(dsv^(xzib6wcwi$-xz724hz^sy+!k'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ptc_db',
        'USER': 'ptc_user',
        'PASSWORD': '13861386',
        'HOST': 'db',  
        'PORT': '5432',
    }
}