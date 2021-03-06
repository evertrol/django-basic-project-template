# Local Django settings for api project.
# This file contains settings that are *for this server* only.

# For example, if this is your development server, DEBUG
# will likely be True, while if this is the production
# server, they would be False.

# This file is *never* checked in into any repository. Therefore,
# email addresses and password will be stored in this file (and not in
# base.py).

# Note that the databases are also defined here: the development
# server can run with sqlite, while the production may use postgresql
# instead.

# Anything that is defined in base.py but for which you'd like another
# value, you can override here.

import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'


ADMINS = []
MANAGERS = ADMINS

DEBUG = True
SEND_BROKEN_LINK_EMAILS = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database', '{{ project_name }}.db')
    },
}

#DATABASE_ROUTERS =


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
ALLOWED_IPS = []



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Amsterdam'
DATE_FORMAT = 'j-n-Y'
DATETIME_FORMAT = 'j-n-Y H:i'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'staticfiles'),
)


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.server.wsgi.application'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
