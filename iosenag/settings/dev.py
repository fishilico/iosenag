# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Activate admin app
INSTALLED_APPS = list(INSTALLED_APPS) + [
    'django.contrib.admin',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite'),
    }
}

ALLOWED_HOSTS = ['127.0.0.1', '[::1]', 'localhost']