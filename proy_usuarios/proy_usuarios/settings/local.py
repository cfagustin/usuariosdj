
"""
 IMPORTAMOS EL ARCHIVO (base.py)
 .base : Ya que estamos en el mismo nivel
 *     : Para que nos incluya todo lo que esta en el archivo (base.py)
"""
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '35@mvx^#&=-e%gig_0u#cii(a3u!9j#asef^&+tl1lo@$ets)a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

# PARA LOS ARCHIVOS MULTIMEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
