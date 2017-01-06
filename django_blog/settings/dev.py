from .base import *

DEBUG = True

SECRET_KEY = 'dev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jh_blog',
        'USER': 'root',
        'PASSWORD': 'm2a1s2u!@#',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

