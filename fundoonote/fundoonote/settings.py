"""
Django settings for fundoonote project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ
from decouple import config
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# logger setting
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s',level=logging.INFO)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
# SECRET_KEY = 'op--q*tjp&z4%0u0=jw%ac2ds=7l4-xq8f650bfd1u&==1e7&t'
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
  # import the app module
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',  # this is used to create the UML Diagram
    'social_django', # social django library is used for social login
    'rest_framework_swagger',
    'fundooapp', # app
    'storages',
    'django_filters', # django filters
    'rest_auth',  # rest_auth is used to creating the API endpoints
    'allauth',
    'allauth.account',
    'django.contrib.sites', # django site domain
    'django_elasticsearch_dsl',  # ElasticSearch DSL is a high level library which is use to writing the qu
    'django_elasticsearch_dsl_drf',
    'django_celery_beat',
'django_email_queue.apps.DjangoEmailQueueConfig'
]
SITE =2
env = environ.Env(
    SECRET_KEY=str,
    DEBUG=(bool, False),
    DATABASE_URL=str,
    search_url =str,
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

ACCOUNT_EMAIL_VERIFICATION = 'None'
ACCOUNT_EMAIL_REQUIRED = True

REST_FRAMEWORK = {
# 'DEFAULT_PERMISSION_CLASSES': (
#          'rest_framework.permissions.IsAuthenticated',
#      ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication', #Token Authentication
        'rest_framework_simplejwt.authentication.JWTAuthentication',# JWT Token
        'rest_framework.authentication.SessionAuthentication',
    ),
     'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}


SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')       # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET') # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] #

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'fundoonote.urls'

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'social_django.context_processors.backends', # add this
                ],
            },
        },
    ]

WSGI_APPLICATION = 'fundoonote.wsgi.application'

EMAIL_BACKEND = 'django_email_queue.backends.EmailBackend'
EMAIL_QUEUE_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'



""" Redis cache """

CACHES = {
    'default': env.cache('REDIS_URL'),
}

""" Database setting using env variable """

DATABASES = {
    'default': env.db()
}

""" Elastic Search"""

ELASTICSEARCH_DSL = {
    'default': {
        'hosts':os.getenv('ELASTIC_SEARCH')
    }

}
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STATICFILES_DIRS = [STATIC_DIR]
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_SSL = True
""" Configuring the authentication classes """
AUTHENTICATION_BACKENDS = [
        'social_core.backends.linkedin.LinkedinOAuth2',
        'social_core.backends.facebook.FacebookOAuth2',
        'django.contrib.auth.backends.ModelBackend',
        'social_core.backends.github.GithubOAuth2',

]

""" The LOGIN_REDIRECT_URL will be used to redirect the 
user after authenticating from Django Login and Social Auth."""
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

# LInkedIn Settings
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = config('SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY')         #Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = config('SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET') #Client Secret
SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_liteprofile', 'r_emailaddress','w_member_social']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'formatted-name', 'public-profile-url', 'picture-url']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
        ('id', 'id'),
        ('formattedName', 'name'),
        ('emailAddress', 'email_address'),
        ('pictureUrl', 'picture_url'),
        ('publicProfileUrl', 'profile_url'),
    ]

# Github settings
SOCIAL_AUTH_GITHUB_KEY = config('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET')

