Automatic Django configuration and utilities for Heroku
=======================================================

Quickstart
----------

Simplify Django configuration in two easy steps:

Include ``django-herokuify`` and ``pylibmc`` packages in your
``requirements.txt`` file.

In the Django ``settings.py`` of your Heroku project add:

  .. code-block:: py

    import herokuify

    from herokuify.common import *              # Common settings, SSL proxy header
    from herokuify.aws import *                 # AWS access keys as configured in env
    from herokuify.mail.mailgun import *        # Email settings for Mailgun add-on

    DATABASES = herokuify.get_db_config()       # Database config
    CACHES = herokuify.get_cache_config()       # Cache config for Memcache/MemCachier


Additionally, you can use storage backends that works well with Amazon S3
and Django Compressor:

  .. code-block:: py

    DEFAULT_FILE_STORAGE = "herokuify.storage.S3MediaStorage"
    MEDIA_URL = "https://{0}.s3.amazonaws.com/media/".format(AWS_STORAGE_BUCKET_NAME)

    STATICFILES_STORAGE = "herokuify.storage.CachedS3StaticStorage"
    STATIC_URL = "https://{0}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)

    COMPRESS_STORAGE = "herokuify.storage.CachedS3StaticStorage"
    COMPRESS_OFFLINE = True

Note: The ``pylibmc`` package entry in your project's root ``requirements.txt``
file is necessary for Heroku Django buildpack to properly configure
the ``libmemcached`` C dependency.

Documentation
-------------

See docs for more information:
`django-herokuify.readthedocs.org <https://django-herokuify.readthedocs.org/>`_

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

License
-------

`django-herokuify` is released under the BSD license.

Other Resources
---------------

- GitHub repository - https://github.com/nigma/django-herokuify
- PyPi Package site - http://pypi.python.org/pypi/django-herokuify
- `Distutils dev version link <https://github.com/nigma/django-herokuify/tarball/develop#egg=django-herokuify-dev>`_
