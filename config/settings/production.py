import os
from .base import * 

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'production secret key: 1234-test')

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '127.0.0.1', 'localhost']

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

STATIC_ROOT = BASE_DIR / 'staticfiles'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

