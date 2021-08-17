from django.core.cache import cache
from micawber.providers import Provider, bootstrap_basic

oembed_providers = bootstrap_basic(cache)
