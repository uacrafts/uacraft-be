from settings.base import *

INSTALLED_APPS += [
    # extra apps
    'corsheaders',
    'rest_framework',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rest_framework.authtoken',
    'django_extensions',
    'anymail',

    # custom apps
    'apps.users.apps.UsersConfig',
    'apps.products.apps.ProductsConfig',
]

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Cors headers
# https://pypi.org/project/django-cors-headers/

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_ALLOWED_ORIGINS = [
    'https://craft-land-top-student-4ee3c794.koyeb.app',
    'https://drf-on-koyeb.craft-land.koyeb',
]

CSRF_TRUSTED_ORIGINS = [
    'https://craft-land-top-student-4ee3c794.koyeb.app',
    'https://drf-on-koyeb.craft-land.koyeb',
]

# DRF
# https://www.django-rest-framework.org/
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# SPECTACULAR
# https://drf-spectacular.readthedocs.io/en/latest/readme.html
SPECTACULAR_SETTINGS = {
    'TITLE': 'Craft Land API',
    'DESCRIPTION': 'DRF Craft Land',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,

    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'CONTACT': {
        'name': 'Stanislav',
        'LinkedIn': 'https://www.linkedin.com/in/stanislav-nikitenko/',
        'telegram': 'https://t.me/F_redy'
    },
}

DEVELOPMENT_ENVIRONMENT = 'development'
PRODUCTION_ENVIRONMENT = 'production'

ENVIRONMENT = env('ENVIRONMENT')

# Django-Anymail
# https://anymail.dev/en/stable/installation/

ANYMAIL = {
    'MAILGUN_API_KEY': '<your Mailgun key>',
}

if ENVIRONMENT == DEVELOPMENT_ENVIRONMENT:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    # Выбрать сервис для отправки email на production
    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

DEFAULT_FROM_EMAIL = 'example@example.com'
SERVER_EMAIL = 'example-server@example.com'

FRONTEND_HOST = env('FRONTEND_HOST', default='http://localhost:8000/')
FRONTEND_CONFIRM_EMAIL_PATH = env('FRONTEND_CONFIRM_EMAIL_PATH', default='/confirm-email/{uid}/{token}')

AUTH_USER_MODEL = 'users.User'

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
    ]
