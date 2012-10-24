.. django-herokuify documentation master file, created by
   sphinx-quickstart on Mon Oct 22 21:48:26 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Automatic Django configuration and utilities for Heroku
=======================================================

Quickstart
----------

Simplify Django configuration in two easy steps:

1. Include ``django-herokuify`` and ``pylibmc`` packages in your
   ``requirements.txt`` file.

2. In the Django ``settings.py`` of your Heroku project add:

  .. code-block:: py

    import herokuify

    from herokuify.common import *            # Common settings, SSL proxy header
    from herokuify.aws import *             # AWS access keys
    from herokuify.mail.mailgun import *    # Mailgun email add-on settings

    DATABASES = herokuify.get_db_config()   # Database config
    CACHES = herokuify.get_cache_config()   # Memcache config for Memcache/MemCachier

Additionally, you can also use storage backends that works nice with Amazon S3
and Django Compressor:

  .. code-block:: py

    DEFAULT_FILE_STORAGE = "herokuify.storage.S3MediaStorage"
    MEDIA_URL = "https://{0}.s3.amazonaws.com/media/".format(AWS_STORAGE_BUCKET_NAME)

    STATICFILES_STORAGE = "herokuify.storage.CachedS3StaticStorage"
    STATIC_URL = "https://{0}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)

    COMPRESS_STORAGE = "herokuify.storage.CachedS3StaticStorage"
    COMPRESS_OFFLINE = True

Dependencies
------------

``django-herokuify`` installs the following dependencies by default:

- Caching and cache configuration::

   pylibmc>=1.2.3
   django-pylibmc-sasl>=0.2.4
   django-heroku-memcacheify>=0.3

- DB configuration::

    dj-database-url>=0.2.1
    django-heroku-postgresify>=0.2

- Storage backend::

    django-storages>=1.1.5
    boto>=2.6.0

Note: It is necessary include ``pylibmc`` package entry in your project's
root ``requirements.txt`` file. The Heroku Django buildpack checks for this
entry and configures the ``libmemcached`` C build dependency.

Content
-------

.. toctree::
   :maxdepth: 1

   common
   db
   cache
   mail
   aws
   storage
