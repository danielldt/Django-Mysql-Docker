from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #django.db.backends.mysql 
        'NAME': 'reublydb', #local: libraries #server: 
        'USER': 'reubly', #root #root
        'PASSWORD': 'reubly112211', #local: root #server: 
        'HOST': 'db', #local: localhost  #server:
        'PORT': '3306',
    }
}