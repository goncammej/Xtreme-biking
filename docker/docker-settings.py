DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

# Modules in use, commented modules that you won't use
MODULES = [
    'administrator',
    'cart',
    'client',
    'order',
    'payment',
    'store',
]

BASEURL = 'http://10.5.0.1:8000'

APIS = {
    'administrator': 'http://10.5.0.1:8000',
    'cart': 'http://10.5.0.1:8000',
    'client': 'http://10.5.0.1:8000',
    'order': 'http://10.5.0.1:8000',
    'payment': 'http://10.5.0.1:8000',
    'store': 'http://10.5.0.1:8000',
}
