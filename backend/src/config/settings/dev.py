from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# json을 활용하는 방식 (개발용)
SECRETS_DIR = os.path.join(BASE_DIR, 'secrets')
BASE_JSON = os.path.join(SECRETS_DIR, 'base.json')
KEY_FILE = json.loads(open(BASE_JSON).read())
SECRET_KEY = KEY_FILE['django']['SECRET_KEY']

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ALLOW_ALL_ORIGINS = True