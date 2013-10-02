# -*- coding: utf-8 -*-
from .base import *  # pyflakes.ignore

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


SECRET_KEY = "django_tests_secret_key"

CACHE_BACKEND = 'locmem:///'
