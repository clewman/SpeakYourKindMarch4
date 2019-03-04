import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = '6xg5%7yddb5v%%-n7l8@$_27r53bfy0-pbbt2c9js3w#wac0@='
