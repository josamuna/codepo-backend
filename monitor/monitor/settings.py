"""
Django settings for monitor project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cu)hv=ra#w-47j67ln)()mf7v$jrwd3ir@9%ts3x-z7jk40$p('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Enabled Django Timezone

# ALLOWED_HOSTS = [
#     # '192.168.43.246',
#     'localhost',
#     '127.0.0.1'
# ]

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = False
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'monitor_engine.apps.MonitorEngineConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_beat',
    "django_webserver"
    # 'channels',    
]

# Solve BigAutofield issue error
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS256',

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     # 'http://127.0.0.1:3000'
# ]

# CHANNEL_LAYERS = {
#   "default": {
#     "BACKEND": "channels_redis.core.RedisChannelLayer",
#     "CONFIG": {
#       "hosts": [("127.0.0.1", 6379)],
#     },
#   },
# }

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'monitor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ASGI_APPLICATION = "monitor.asgi.application"
WSGI_APPLICATION = 'monitor.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'monitor_db',
        'USER': 'josam',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

CELERY_ENABLE_UTC = True
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_TIMEZONE = 'UTC'
CELERY_BEAT_SCHEDULE = {
    'connect_to_mqtt_broker': {
        'task': 'monitor_engine.tasks.connect_to_mqtt_broker',
        #    'schedule': 1800.0,
        'schedule': 60.0,
        #    'schedule': crontab(hour=11, minute=29, day_of_week=2)
    },

    # 'send-notification-on-friday-afternoon': { 
    #      'task': 'sendmessage.tasks.send_notification', 
    #      'schedule': 30.0#crontab(hour=6, minute=11, day_of_week=2),
    #     }, 
}

# Sensitive data to be keept elsewhere of here

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'EMAIL_HOST'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
DEFAULT_FROM_EMAIL = 'DEFAULT_FROM_EMAIL'

# End Sensitive data

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
