from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #django.db.backends.mysql 
        'NAME': 'db', #local: libraries #server: 
        'USER': 'dbuser', #root #root
        'PASSWORD': 'dbuser112211', #local: root #server: 
        'HOST': 'db', #local: localhost  #server:
        'PORT': '3306',
    }
}