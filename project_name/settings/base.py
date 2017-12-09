# Django settings for api project.

# Make a copy of local_template.py to local.py and edit that copy,
# filling in all the undefined values (or changing them accordingly).
# Do *not* store local.py in your repository

import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
#USE_TZ = True
USE_TZ = False


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'
# URL that handles the media served from STATIC_ROOT. Make sure to use a
# trailing slash.
STATIC_URL = '/static/'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'{{ project_name }}.apps.<app-name>',
]

ROOT_URLCONF = '{{ project_name }}.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CommonMiddleware settings
APPEND_SLASH = True
#PREPEND_WWW = True


# ensure large uploaded files end up with correct permissions. See
# http://docs.djangoproject.com/en/dev/ref/settings/#file-upload-permissions
FILE_UPLOAD_PERMISSIONS = 0o664


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                #'django.template.context_processors.media',
                #'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# login URL for auth app
#LOGIN_URL = '/account/login/'

TEMPLATE403 = '403.html'
