"""
Django settings for cbgrandslam project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o0n*(r)k6w(ty3n+%3vw=ut_04c&1agve457*p^8jywq2yqn^u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'game'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cbgrandslam.urls'

WSGI_APPLICATION = 'cbgrandslam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',    # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'grandslam.db',           # Or pathto database file if using sqlite3.
        #'USER': 'root',                  # Not used with sqlite3.
        #'PASSWORD': '',                  # Not used with sqlite3.
        #'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '',                         # Or pathto database file if using sqlite3.
#    }
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'orcl',
        'USER': 'system',
        'PASSWORD': 'Oracle123',
        'HOST': '127.0.0.1',
        'PORT': '1521',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
