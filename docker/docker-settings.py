DEBUG = True

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['http://10.5.0.1:8000', 'http://localhost:8000' ]

BASEURL = 'http://10.5.0.1:8000'
