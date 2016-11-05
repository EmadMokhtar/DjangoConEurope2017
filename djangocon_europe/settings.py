"""
Django settings for djangocon_europe project.

Generated by 'django-admin startproject' using Django 1.8.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os

import environ

gettext = lambda s: s

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env()

BASE_DIR = root()
DATA_DIR = root.path('dist/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition

ROOT_URLCONF = 'djangocon_europe.urls'

WSGI_APPLICATION = 'djangocon_europe.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = DATA_DIR('media')
STATIC_ROOT = DATA_DIR('static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'djangocon_europe', 'static'),
)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'djangocon_europe', 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',
                'conference.context_processors.context_settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_link',
    'reversion',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_googlemap',
    'djangocms_video',
    'aldryn_video',
    'djangocon_europe',
    'robots',
    'djangocms_page_meta',
    'aldryn_apphooks_config',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'meta_mixin',
    'djangocms_blog',

    ## Nephila widgets

    'nephila_widgets',
    'nephila_widgets.base',
    'nephila_widgets.conf',
    'nephila_widgets.files',
    'nephila_widgets.advanced',
    'nephila_widgets.design',
    'nephila_widgets.design.jessica',
    'nephila_widgets.utils',

    ## Third part

    'import_export',
    'compressor',
    'clear_cache',
    'djmail',

    ## DjangoCon related application
    'conference.cfp',
    'conference.helpers',
]

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('home.html', 'Homepage'),
    ('internal.html', 'Internal Page'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': env.db(),
}

CACHES = {
    'default': env.cache(),
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background'
)

NPH_DESIGN = 'jessica'

WIDGETS_PLUGIN_TEMPLATES = {}

WIDGETS_PLUGIN_TEMPLATES['WidgetsSectionPlugin'] = (
    ('layout/section_purple.html', 'Purple Section'),
    ('layout/section_yellow.html', 'Yellow Section'),
    ('layout/section_sponsors.html', 'Sponsors Section'),
)

WIDGETS_PLUGIN_TEMPLATES['WidgetsImagePlugin'] = (
    ('files/image_full.html', 'Base template'),
    ('files/image_before_text.html', 'Image before text'),
    ('files/image_after_text.html', 'Image after text'),
    ('files/sponsor.html', 'Sponsor'),
    ('files/cast.html', 'Cast'),
)

try:
    import raven

    if env('SENTRY_DSN'):
        RAVEN_CONFIG = {
            'dsn': env('SENTRY_DSN'),
            # If you are using git, you can also automatically configure the
            # release based on the git info.
            'release': raven.fetch_git_sha(os.path.dirname(os.path.dirname(__file__))),
        }
        INSTALLED_APPS.append('raven.contrib.django.raven_compat')
except:
    pass

GOOGLE_ANALYTICS_ID = 'UA-29840573-18'

DEFAULT_FROM_EMAIL = 'DjangoCon Europe 2017 <2017@djangocon.eu>'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_BACKEND = 'djmail.backends.default.EmailBackend'
DJMAIL_REAL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

META_USE_SITES = True
META_SITE_PROTOCOL = 'https'
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True
META_TWITTER_TYPE = 'summary'
META_TWITTER_SITE = '@DjangoConEurope'
META_FB_TYPE = 'Article'
META_GPLUS_SCOPE_CATEGORY = 'Article'
BLOG_TWITTER_AUTHOR = '@DjangoConEurope'