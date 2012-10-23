#-*- coding: utf-8 -*-

from __future__ import unicode_literals

__all__ = [
    "SECURE_PROXY_SSL_HEADER"
]

#: SSL proxy header as defined in
#: `Django settings docs <https://docs.djangoproject.com/en/1.4/ref/settings/#secure-proxy-ssl-header>`_.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
