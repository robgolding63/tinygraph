# Django settings for tinygraph project.

import os
import sys

# An absolute path to the root directory of the Django project, this directory
# is the one whoch would normally contain manage.py
SITE_ROOT = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

# The directory within (for organisational convenience) which all Django apps
# are situated.
APP_DIR = os.path.join(SITE_ROOT, 'apps')

# Absolute path to the directory which holds the static files
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

# The URL at which static files should be served from
STATIC_URL = '/static/'

MIB_ROOT = os.path.join(SITE_ROOT, 'mibs')

# Add the "apps" folder to the path so I don't have to constants imports like
# apps.myapp.file, now I can do just myapp.file
sys.path.insert(0, APP_DIR)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(SITE_ROOT, 'dev.db'),
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': '',
        # 'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&lwm#fx#1yt67ojg1y1k+(&h77zeby2(i77%b=*^t-g-gqvqog'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'context_processors.static',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'tinygraph.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
    'core',
    'devices',
    'definitions',
    'rules',
    'data',
    'dashboard',
    'api',
)

# Tells pysnmp where the user uploaded (converted) mib files are
os.environ['PYSNMP_MIB_DIR'] = MIB_ROOT

# For debug toolbar.
if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INTERNAL_IPS = ('127.0.0.1',)
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

TINYGRAPH_SNMP_GETBULK_SIZE = 10
TINYGRAPH_TINYGRAPH_LOG_FILENAME = '/tmp/tinygraph.log'
TINYGRAPH_TINYGRAPHD_LOG_FILENAME = '/var/log/tinygraphd.log'
TINYGRAPH_POLL_INTERVAL = 5 # minutes