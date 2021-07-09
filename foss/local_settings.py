LOCAL_DEBUG = True

LOCAL_SECRET_KEY = 'someSecretKeyHere'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/socialstream',
        'TIMEOUT': 60 * 60,
        'OPTIONS': {'MAX_ENTRIES': 1000}
    },
}

""" optional dummy cache for development
It use cache wiring, but doesn't use a cache
"""

"""
CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
}
"""

