from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# 환경 변수 활용 (배포용)
def get_env_variable(var_name):
  """환경 변수를 가져오거나 예외를 반환한다."""
  try:
    return os.environ[var_name]
  except KeyError:
    error_msg = "Set the {} environment variable".format(var_name)
    raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

