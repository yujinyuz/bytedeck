"""
Django settings for hackerspace_online project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

# https://django-environ.readthedocs.io/en/latest/#django-environ
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list)
)

project_root = environ.Path(__file__) - 3  # "/"
PROJECT_ROOT = project_root()
BASE_DIR = project_root('src')  # "/src/"

# read in the .env file
environ.Env.read_env(os.path.join(project_root(), '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

WSGI_APPLICATION = 'hackerspace_online.wsgi.application'

# Application definition
SHARED_APPS = (
    'tenant_schemas',
    'tenant',
    'django.contrib.contenttypes',

    # WHY ARE THESE NEEDED IN BOTH SHARED AND TENANT APPS LISTS?
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.flatpages',
    ###########################################

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # tenant beat is not supported, have to do it manually with:
    # https://github.com/maciej-gol/tenant-schemas-celery#celery-beat-integration
    # or
    # https://github.com/maciej-gol/tenant-schemas-celery/issues/34
    # by inserting the schema into the task headers so that tenant-schams-celery knows where to run it
    'django_celery_beat',

    'django.contrib.sites',

    'grappelli',
    'crispy_forms',
    'bootstrap_datepicker_plus',
    'embed_video',
    'django_select2',
    'jchart',
    'url_or_relative_url_field',
    'import_export',
    'colorful',

)

TENANT_APPS = (
    'django.contrib.contenttypes',

    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # tenant beat is not supported, have to do it manually with:
    # https://github.com/maciej-gol/tenant-schemas-celery#celery-beat-integration
    # or
    # https://github.com/maciej-gol/tenant-schemas-celery/issues/34
    # by inserting the schema into the task headers so that tenant-schams-celery knows where to run it
    'django_celery_beat',

    'hackerspace_online',
    'django_summernote',

    'quest_manager',
    'profile_manager',
    'announcements',
    'comments',
    'notifications',
    'courses',
    'prerequisites',
    'badges',
    'djcytoscape',
    'portfolios',
    'utilities',
    'siteconfig',
)


INSTALLED_APPS = (
    'tenant_schemas',
    'tenant.apps.TenantConfig',

    # http://django-grappelli.readthedocs.org/en/latest/quickstart.html
    'grappelli',

    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',  # for allauth
    'django.contrib.staticfiles',

    'django.contrib.flatpages',  # https://docs.djangoproject.com/en/1.10/ref/contrib/flatpages/

    # third party apps

    # https://django-allauth.readthedocs.org/en/latest/installation.html
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',

    # http://django-crispy-forms.readthedocs.org/en/latest/install.html
    'crispy_forms',

    # https://github.com/summernote/django-summernote
    'django_summernote',

    # https://github.com/monim67/django-bootstrap-datepicker-plus
    'bootstrap_datepicker_plus',

    # https://github.com/yetty/django-embed-video
    # used for the EmbedVideoField that validates YouTube and Vimeo urls
    'embed_video',

    # https://github.com/applegrew/django-select2
    'django_select2',

    # https://github.com/matthisk/django-jchart
    'jchart',

    # https://github.com/timonweb/django-url-or-relative-url-field
    'url_or_relative_url_field',

    # https://django-import-export.readthedocs.io
    'import_export',

    'django_celery_beat',

    # https://github.com/charettes/django-colorful
    'colorful',

    # hackerspace_online.apps.HackerspaceConfig
    'hackerspace_online',

    # local apps
    'quest_manager',
    'profile_manager',
    'announcements',
    'comments',
    'notifications',
    'courses',
    'prerequisites',
    'badges',
    'djcytoscape',
    'portfolios',
    'utilities',
    'siteconfig',
)

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    # caching: https://docs.djangoproject.com/en/1.10/topics/cache/
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # used by django-date-time-widget
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'hackerspace_online.urls'

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

                'hackerspace_online.context_processors.config',
            ],
            # 'string_if_invalid': 'DEBUG WARNING: undefined template variable [%s] not found',
        },
    },
]

# REDIS AND CACHES #################################################

REDIS_HOST = env('REDIS_HOST', default='127.0.0.1')  # os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = env('REDIS_PORT')  # os.environ.get('REDIS_PORT', '6379')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        'KEY_FUNCTION': 'tenant_schemas.cache.make_key',
        'REVERSE_KEY_FUNCTION': 'tenant_schemas.cache.reverse_key'
    },
    'select2': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': None,
        'KEY_FUNCTION': 'tenant_schemas.cache.make_key'
    }
}
SELECT2_CACHE_BACKEND = 'default'


# I18N AND L10N ####################################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Vancouver'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# CELERY ####################################################################

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_MAX_RETRIES = 10
CELERY_TASKS_BUNCH_SIZE = 10

# allowed delay between conditions met updates for all users:
# In sec., wait before start next 'big' update for all conditions, if it's going to start - all other updates could be skipped
CONDITIONS_UPDATE_COUNTDOWN = 60 * 1  


# DATABASES #######################################################

POSTGRES_HOST = env('POSTGRES_HOST', default='127.0.0.1')  # os.environ.get('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT = env('POSTGRES_PORT')
POSTGRES_DB_NAME = env('POSTGRES_DB_NAME')
POSTGRES_USER = env('POSTGRES_USER')
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD', default=None)

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': POSTGRES_DB_NAME,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT
    }
}

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

# EMAIL ######################################

EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.filebased.EmailBackend')
EMAIL_FILE_PATH = env('EMAIL_BACKEND', default=os.path.join(PROJECT_ROOT, "_sent_mail"))

EMAIL_HOST = env('EMAIL_HOST', default=None)
EMAIL_HOST_USER = env('EMAIL_HOST', default=None)
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default=None)

EMAIL_PORT = env('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=True)

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default=None)

# SERVER ERRORS EMAIL
admins_raw = env('ADMINS', default=[])
if admins_raw:
    # https://django-environ.readthedocs.io/en/latest/index.html?highlight=ADMINS#nested-lists
    ADMINS = [tuple(entry.split(':')) for entry in env.list('ADMINS')] 
SERVER_EMAIL = env('SERVER_EMAIL', default=None)


# STATIC AND MEDIA ###########################

# Urls to display media and static, e.g. example.com/media/
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# The absolute path to the directory where uploaded media files will be saved to
MEDIA_ROOT = env('MEDIA_ROOT', default=os.path.join(PROJECT_ROOT, "_media_uploads"))

# The absolute path to the directory where `collectstatic` will move the static files to.
STATIC_ROOT = env('STATIC_ROOT', default=os.path.join(PROJECT_ROOT, "_collected_static"))

STATICFILES_DIRS = env(
    'STATICFILES_DIRS', 
    default=(
        os.path.join(BASE_DIR, "static"),
        # '/var/www/static/',
    )
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID = 1

# https://github.com/charettes/django-colorful
GRAPPELLI_CLEAN_INPUT_TYPES = False


# TENANTS ###############################################################

TENANT_MODEL = "tenant.Tenant"

TENANT_DEFAULT_SUPERUSER_USERNAME = env('TENANT_DEFAULT_SUPERUSER_USERNAME')
TENANT_DEFAULT_SUPERUSER_PASSWORD = env('TENANT_DEFAULT_SUPERUSER_PASSWORD')

# See this: https://github.com/timberline-secondary/hackerspace/issues/388
# The design choice for media files it serving all the media files from one directory instead of separate directory for each tenant. 
SILENCED_SYSTEM_CHECKS = ['tenant_schemas.W003']


# AUTHENTICATION ##################################################

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

# AllAuth Configuration
# SOCIALACCOUNT_PROVIDERS = \
#     {'facebook':
#          {'SCOPE': ['email', 'public_profile'],
#           'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#           'METHOD': 'oauth2',
#           # 'LOCALE_FUNC': 'path.to.callable',
#           'VERIFIED_EMAIL': False,
#           'VERSION': 'v2.3'}
#      }

# https://django-allauth.readthedocs.org/en/latest/configuration.html
LOGIN_REDIRECT_URL = '/'
# https://stackoverflow.com/questions/44571373/python-3-6-django1-10-login-required-decorator-redirects-to-link-with-missing/44571408#44571408
LOGIN_URL = 'account_login'
# ACCOUNT_ADAPTER #(=”allauth.account.adapter.DefaultAccountAdapter”)
# Specifies the adapter class to use, allowing you to alter certain default behaviour.
ACCOUNT_AUTHENTICATION_METHOD = "username"  # (=”username” | “email” | “username_email”)
# Specifies the login method to use – whether the user logs in by entering their username, 
# e-mail address, or either one of both. Setting this to “email” requires ACCOUNT_EMAIL_REQUIRED=True
# ACCOUNT_CONFIRM_EMAIL_ON_GET #(=False)
# Determines whether or not an e-mail address is automatically confirmed by a mere GET request.
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL #(=settings.LOGIN_URL)
# The URL to redirect to after a successful e-mail confirmation, in case no user is logged in.
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL  # (=None)
# The URL to redirect to after a successful e-mail confirmation, in case of an authenticated user. Set to None to use settings.LOGIN_REDIRECT_URL.
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS #(=3)
# Determines the expiration date of email confirmation mails (# of days).
# ACCOUNT_EMAIL_REQUIRED = True #(=False)
# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_VERIFICATION = None  # (=”optional”)
# Determines the e-mail verification method during signup – choose one of “mandatory”, “optional”, or “none”. When set to “mandatory”
# the user is blocked from logging in until the email address is verified. Choose “optional” or “none” to allow logins with an unverified 
# e-mail address. In case of “optional”, the e-mail verification mail is still sent, whereas in case of “none” no e-mail verification mails are sent.
# ACCOUNT_EMAIL_SUBJECT_PREFIX #(=”[Site] ”)
# Subject-line prefix to use for email messages sent. By default, the name of the current Site (django.contrib.sites) is used.
# ACCOUNT_DEFAULT_HTTP_PROTOCOL  #(=”http”)
# The default protocol used for when generating URLs, e.g. for the password forgotten procedure. Note that this is a default only – 
# see the section on HTTPS for more information.
# ACCOUNT_FORMS #(={})
# Used to override forms, for example: {‘login’: ‘myapp.forms.LoginForm’}
ACCOUNT_FORMS = {'signup': 'hackerspace_online.forms.CustomSignupForm'}
# ACCOUNT_LOGOUT_ON_GET #(=False)
# Determines whether or not the user is automatically logged out by a mere GET request. See documentation for the LogoutView for details.
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True  # (=False)
# Determines whether or not the user is automatically logged out after changing the password. See documentation for Django’s session invalidation
#  on password change. (Django 1.7+)
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL  # (=”/”)


#################################
#
# SUMMERNOTE WYSIWYG EDITOR
# https://github.com/summernote/django-summernote
#
#################################

SUMMERNOTE_THEME = 'bs3'
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    # Or, you can set it as False to use SummernoteInplaceWidget by default - no iframe mode
    # In this case, you have to load Bootstrap/jQuery stuff by manually.
    # Use this when you're already using Bootstraip/jQuery based themes.
    # 'iframe': False,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '480',

        'followingToolbar': False,

        # Customize toolbar buttons
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'superscript', 'subscript',
                      'strikethrough', 'add-text-tags', 'clear']],
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'listStyles', 'paragraph']],
            # ['height', ['height']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'videoAttributes', 'hr', 'faicon', 'math', ]],  # , 'nugget']],
            ['view', ['codeview']],
            ['help', ['help']],
        ],

        # You can also add custom settings for external plugins
        # 'print': {
        #     'stylesheetUrl': '/some_static_folder/printable.css',
        # },
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            'lineWrapping': 'true',
            # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            'theme': 'monokai',
        },

    },

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,
    'attachment_filesize_limit': 4096 * 4096,

    # Set `upload_to` function for attachments.
    # 'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
    # 'attachment_storage_class': 'my.custom.storage.class.name',

    # Set custom model for attachments (default: 'django_summernote.Attachment')
    # 'attachment_model': 'my.custom.attachment.model',  # must inherit 'django_summernote.AbstractAttachment'

    # You can disable attachment feature.
    # Currently only works for images anyway.  Turn on when it works with other files
    # Images can still be embedded with the image tool
    'disable_attachment': False,

    # Set `True` to return attachment paths in absolute URIs.
    'attachment_absolute_uri': False,

    # You can also add custom css/js for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    'css_for_inplace': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
        # os.path.join(STATIC_URL, 'css/custom_summernote_widget.css'),
        os.path.join(STATIC_URL, 'summernote-faicon/summernote-ext-faicon.css'),
        # os.path.join(STATIC_URL, 'summernote-ext-emoji-ajax/summernote-ext-emoji-ajax.css'),
        os.path.join(STATIC_URL, 'summernote-add-text-tags/summernote-add-text-tags.css'),
        os.path.join(STATIC_URL, 'summernote-list-styles/summernote-list-styles.css'),
        os.path.join(STATIC_URL, 'css/custom_summernote_widget.css'),
        '//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css',
    ),
    'js_for_inplace': (
        os.path.join(STATIC_URL, 'summernote-faicon/summernote-ext-faicon.js'),
        # os.path.join(STATIC_URL, 'summernote-ext-emoji-ajax/summernote-ext-emoji-ajax.js'),
        os.path.join(STATIC_URL, 'js/summernote-video-attributes.js'),
        os.path.join(STATIC_URL, 'summernote-add-text-tags/summernote-add-text-tags.js'),
        os.path.join(STATIC_URL, 'js/summernote-image-shapes.js'),
        os.path.join(STATIC_URL, 'summernote-list-styles/summernote-list-styles.js'),
        os.path.join(STATIC_URL, 'js/summernote-table-styles.js'),
        os.path.join(STATIC_URL, 'js/summernote-table-headers.js'),
        # '//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.js', # included in base template
        os.path.join(STATIC_URL, 'js/summernote-math.js'),
    ),

    # Codemirror as codeview
    # If any codemirror settings are defined, it will include codemirror files automatically.
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
        os.path.join(STATIC_URL, 'css/font-awesome.min.css'),
        os.path.join(STATIC_URL, 'css/custom_common.css'),
        os.path.join(STATIC_URL, 'css/custom.css'),
        os.path.join(STATIC_URL, 'css/custom_summernote_iframe.css'),
        os.path.join(STATIC_URL, 'summernote-faicon/summernote-ext-faicon.css'),
        # os.path.join(STATIC_URL, 'summernote-ext-emoji-ajax/summernote-ext-emoji-ajax.css'),
        os.path.join(STATIC_URL, 'summernote-add-text-tags/summernote-add-text-tags.css'),
        os.path.join(STATIC_URL, 'summernote-list-styles/summernote-list-styles.css'),
        '//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css',
    ),

    # To use external plugins,
    # Include them within `css` and `js`.
    'js': (
        os.path.join(STATIC_URL, 'summernote-faicon/summernote-ext-faicon.js'),
        # os.path.join(STATIC_URL, 'summernote-ext-emoji-ajax/summernote-ext-emoji-ajax.js'),
        os.path.join(STATIC_URL, 'js/summernote-video-attributes.js'),
        os.path.join(STATIC_URL, 'summernote-add-text-tags/summernote-add-text-tags.js'),
        os.path.join(STATIC_URL, 'js/summernote-image-shapes.js'),
        os.path.join(STATIC_URL, 'summernote-list-styles/summernote-list-styles.js'),
        os.path.join(STATIC_URL, 'js/summernote-table-styles.js'),
        os.path.join(STATIC_URL, 'js/summernote-table-headers.js'),
        '//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.js',
        os.path.join(STATIC_URL, 'js/summernote-math.js'),
    ),

    'popover': {
        'image': [
            ['custom', ['imageShapes']],
            ['imagesize', ['imageSize100', 'imageSize50', 'imageSize25']],
            ['float', ['floatLeft', 'floatRight', 'floatNone']],
            ['remove', ['removeMedia']]
        ],
        'link': [
            ['link', ['linkDialogShow', 'unlink']]
        ],
        'table': [
            ['add', ['addRowDown', 'addRowUp', 'addColLeft', 'addColRight']],
            ['delete', ['deleteRow', 'deleteCol', 'deleteTable']],
            ['custom', ['tableHeaders', 'tableStyles']]
        ],
    },

    # Lazy initialize
    # If you want to initialize summernote at the bottom of page, set this as True
    # and call `initSummernote()` on your page.
    # 'lazy': True,

}


# DEBUG / DEVELOPMENT SPECIFIC SETTINGS #################################

if DEBUG:

    INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

    # DEBUG TOOLBAR
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    INSTALLED_APPS += (
        'debug_toolbar',
        'template_timings_panel',
        # http://django-cachalot.readthedocs.io
        # 'cachalot',
    )
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'template_timings_panel.panels.TemplateTimings.TemplateTimings',
        # 'cachalot.panels.CachalotPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]


# TESTING ##################################################

TESTING = 'test' in sys.argv
if TESTING:
    # Use weaker password hasher for speeding up tests (when tested)
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]
