#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from memcacheify import memcacheify

def get_cache_config():
    """Return a fully configured Django ``CACHES`` setting.

    Scans environment variables for available memcache addon.
    Additionally includes Django's LocMemCache backend under ``"locmem"``
    cache name.
    """
    caches = memcacheify()
    caches["locmem"] = {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    }
    return caches
