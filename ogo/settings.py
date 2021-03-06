"""
Django settings for OGO
"""
import os.path
import yaml

########################################################################################################################
# Override the following in ../private.yml:
LOCAL_SETTINGS = """
DATABASE:
    NAME: ogo
DEBUG: false
SECRET_KEY:
# Car Share Everywhere API endpoint
CSE_API_ENDPOINT:
# Cache setting - set to a string prefix to enable redis cache use:
USE_REDIS_CACHE_PREFIX:
ALLOWED_HOSTS:
    - www.ogocarshare.ca
# Is an https connection available?
HTTPS_AVAILABLE: true
# Google Analytics account to use, e.g. UA-12345678-1
GOOGLE_ANALYTICS_ACCOUNT:
"""

########################################################################################################################

OGO_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(OGO_ROOT, os.path.pardir))

# Update LOCAL_SETTINGS:
LOCAL_SETTINGS = yaml.load(LOCAL_SETTINGS)
with open(PROJECT_ROOT + "/private.yml") as fh:
    LOCAL_SETTINGS.update(yaml.load(fh.read()))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '',
    }
}
DATABASES['default'].update(LOCAL_SETTINGS['DATABASE'])

if LOCAL_SETTINGS['USE_REDIS_CACHE_PREFIX']:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': LOCAL_SETTINGS.get('REDIS_URL', 'redis://127.0.0.1:6379/1'),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
            'KEY_PREFIX': LOCAL_SETTINGS['USE_REDIS_CACHE_PREFIX'],
        }
    }
else:
    CACHES = {
        'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
    }
########################################################################################################################

DEBUG = LOCAL_SETTINGS['DEBUG']

ADMINS = (
    ('Braden MacDonald', 'webmaster@ogocarshare.ca'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = LOCAL_SETTINGS['ALLOWED_HOSTS']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Vancouver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

FIXTURE_DIRS = (os.path.join(OGO_ROOT, "fixtures"), )

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = LOCAL_SETTINGS.get('MEDIA_ROOT', os.path.join(PROJECT_ROOT, "user_media"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = LOCAL_SETTINGS.get('STATIC_ROOT', os.path.join(PROJECT_ROOT, "site_media"))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(OGO_ROOT, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Whether Django should serve media files (user uploads) with its built-in server
SERVE_MEDIA_FILES = LOCAL_SETTINGS.get('SERVE_MEDIA_FILES', DEBUG)

# Is an https connection available?
HTTPS_AVAILABLE = LOCAL_SETTINGS['HTTPS_AVAILABLE']

# Make this unique, and don't share it with anybody.
SECRET_KEY = LOCAL_SETTINGS['SECRET_KEY']

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'ogo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ogo.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': (
            os.path.join(OGO_ROOT, "templates"),
        ),
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                # 'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'ogo.utils.context_processors.ogo_globals',
            ),
        }
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'reversion',
    'easy_thumbnails',
    'filer',
    'sekizai',
    'compressor',
    'bootstrapform',
    # CMS:
    'cms',
    'menus',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_column',
    'cmsplugin_youtube',
    'cmsplugin_html',
    'cmsplugin_img',
    # Blog:
    'aldryn_apphooks_config',
    'cmsplugin_filer_image',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'djangocms_blog',
    # OGO:
    'ogo.plugins',
    'ogo.giftcert',
    'ogo.cms_extensions',
    'ogo.vehicle_details',
)

# Log to console and email the site admins on any 500 error
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
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SERVER_EMAIL = LOCAL_SETTINGS.get('SERVER_EMAIL', 'root@localhost')
EMAIL_HOST = LOCAL_SETTINGS.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = LOCAL_SETTINGS.get('EMAIL_PORT', 587)
EMAIL_HOST_USER = LOCAL_SETTINGS.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = LOCAL_SETTINGS.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = LOCAL_SETTINGS.get('EMAIL_USE_TLS', True)

# Compressor settings:
COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OUTPUT_DIR = 'cache'  # lower-case the default "CACHE"
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'ogo.utils.compressor.SassFilter'),
)
COMPRESS_CSS_FILTERS = (
    'ogo.utils.compressor.CssAutoprefixerFilter',
)
if not DEBUG:
    COMPRESS_OFFLINE = True

# CMS Settings:
CMS_TEMPLATES = (
    ('ogo/cms_page.html', 'OGO Regular Page'),
    ('ogo/cms_page_sectioned.html', 'OGO Sectioned Page'),
)

OGO_CMS_CONTENT_PLUGINS = [
    'TextPlugin',
    'HTMLPlugin',
    'ImagePlugin',
    'YouTubePlugin',
    'CarMapPlugin',
    'CarListPlugin',
    'PartnerPlugin',
    'MultiColumnPlugin',
]

# The purpose of the following complex setting is to require that the top-level plugins on each
# page are either a PageSectionPlugin or a BackgroundImagePlugin
CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': 'Content',
        'plugins': ['PageSectionPlugin', 'BackgroundImagePlugin', 'PartnerLogoSectionPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'PageSectionPlugin',
                'values': {
                    'title': 'Main Section',
                },
            },
        ],
        # We need to explicitly override 'child_classes', or else only the two plugins listed
        # above can be added as children even of those top-level plugins.
        'child_classes': {
            'PageSectionPlugin': OGO_CMS_CONTENT_PLUGINS,
            'BackgroundImagePlugin': OGO_CMS_CONTENT_PLUGINS,
            'ColumnPlugin': OGO_CMS_CONTENT_PLUGINS,
            'MultiColumnPlugin': ('ColumnPlugin', ),
        },
    },
}
for plugin_name in OGO_CMS_CONTENT_PLUGINS:
    CMS_PLACEHOLDER_CONF['content']['child_classes'].setdefault(plugin_name, OGO_CMS_CONTENT_PLUGINS)

# CMS multi-column plugin settings:
COLUMN_WIDTH_CHOICES = (
    ('1', "1/12"),
    ('2', "1/6"),
    ('3', "1/4"),
    ('4', "1/3"),
    ('5', "5/12"),
    ('6', "1/2"),
    ('7', "7/12"),
    ('8', "2/3"),
    ('9', "3/4"),
    ('10', "5/6"),
    ('11', "11/12"),
    ('12', "full"),
)

# Filer settings:
FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': MEDIA_ROOT,
                'base_url': MEDIA_URL,
            },
            'UPLOAD_TO': 'ogo.utils.filer.filer_namer',
            'UPLOAD_TO_PREFIX': 'f',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': MEDIA_ROOT,
                'base_url': MEDIA_URL,
            },
            'THUMBNAIL_OPTIONS': {
                'base_dir': 'thumbs',
            },
        },
    },
}

# Car Share Everywhere API settings:
CSE_API_ENDPOINT = LOCAL_SETTINGS['CSE_API_ENDPOINT']

# Google Analytics:
GOOGLE_ANALYTICS_ACCOUNT = LOCAL_SETTINGS['GOOGLE_ANALYTICS_ACCOUNT']

# Settings required for djangocms-blog:
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
META_SITE_PROTOCOL = 'https' if HTTPS_AVAILABLE else 'http'
META_USE_SITES = True
