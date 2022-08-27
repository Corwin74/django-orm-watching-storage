import os
from environs import Env


env = Env()
env.read_env()


DATABASES = {
    "default": env.dj_db_url('DATABASE_URL')
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('DJANGO_SECRET_KEY', default='--==**Replace_this_key_in_production**==--')
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['.localhost', '127.0.0.1', '[::1]'])

ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
