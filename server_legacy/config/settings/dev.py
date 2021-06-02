from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

# 환경 변수 활용 (배포, 개발용)
def get_env_variable(var_name):
  """환경 변수를 가져오거나 예외를 반환한다."""
  try:
    return os.environ[var_name]
  except KeyError:
    error_msg = "Set the {} environment variable".format(var_name)
    raise ImproperlyConfigured(error_msg)

try:
    # json을 활용하는 방식 (개발용)
    SECRETS_DIR = os.path.join(BASE_DIR, 'secrets')
    BASE_JSON = os.path.join(SECRETS_DIR, 'base.json')
    KEY_FILE = json.loads(open(BASE_JSON).read())
    SECRET_KEY = KEY_FILE['django']['SECRET_KEY']

except FileNotFoundError:
    SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")


ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
