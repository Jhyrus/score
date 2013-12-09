from os.path import realpath, dirname, join

location = lambda x: realpath(
    join(dirname(dirname(realpath(__file__))), x))

ROOT_PATH = location('')
LOG_ROOT = location('../var/log')
DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_default',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/La_Paz'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = location('../public/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = location('../public/static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    location('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b$-%k@c6!rgmtn9)h7x55g-)fw%2xe$ie=7_)$_sw!!vwelp39'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'sekizai.context_processors.sekizai',
)

ROOT_URLCONF = 'finish.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'finish.wsgi.application'

TEMPLATE_DIRS = (
    location('templates'),
)

INSTALLED_APPS = (
    # Django applications
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Third party applications
    'south',
    'pipeline',
    'sekizai',
    'crispy_forms',
    'django_extensions',
    'django_hstore',

    # Current Project applications
    'finish.wall',

)


# Logging ----------------------------------------------------------------------
#

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'general': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(ROOT_PATH, '../var/log/django.log'),
            'maxBytes': 1024 * 1024 * 25,
            'formatter': 'verbose',
            'backupCount': 25, # TODO: Rotate without delete old logs,
            # compress the logs and maybe upload to S3
        },
        'migrations': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(ROOT_PATH, '../var/log/migrations.log'),
            'maxBytes': 1024 * 1024 * 25,
            'formatter': 'simple',
            'backupCount': 25,
        },
        'access': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(ROOT_PATH, '../var/log/access.log'),
            'maxBytes': 1024 * 1024 * 25,
            'formatter': 'verbose',
            'backupCount': 25,
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console','general'],
            'filters': ['require_debug_false'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'migrations': {
            'handlers': ['console', 'migrations'],
            'level': 'INFO',
        }
    }
}

# Static Resources -------------------------------------------------------------

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
    )

STATICFILES_STORAGE = 'finish.core.storage.PipelineCachedStorage'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_YUI_CSS_ARGUMENTS = '--line-break 80'
PIPELINE_YUI_JS_ARGUMENTS = '--line-break 80'

PIPELINE_CSS = {
    'master': {
        'source_filenames': (
            'css/vendor.css',
            'css/master.css',
            ),
        'output_filename': 'css/master.min.css',
    },
}

PIPELINE_JS = {
    'master': {
        'source_filenames': (
            'js/jquery.js',
            'js/bootstrap.js',
            ),
        'output_filename': 'js/master.min.js',
    }
}

COMPASS_PROJECT_PATH = location('static')

# Login / Authentication -------------------------------------------------------

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/accounts/'
LOGIN_ERROR_URL = '/accounts/login-error/'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'