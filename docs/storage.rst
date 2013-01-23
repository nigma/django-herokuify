.. _storage:

.. automodule:: herokuify.storage

Storage Backends
================

Defines S3 bucket subdirectory storage for static and media files and
provides storage backends that are compatible with
`Django Compressor <http://django_compressor.readthedocs.org/en/latest/>`_.


Django config
-------------

To use AWS S3 storage for static and media files set this in your project
settings:

  .. code-block:: py

    STATICFILES_STORAGE = "herokuify.storage.S3StaticStorage"
    STATIC_URL = "https://{0}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)

    DEFAULT_FILE_STORAGE = "herokuify.storage.S3MediaStorage"
    MEDIA_URL = "https://{0}.s3.amazonaws.com/media/".format(AWS_STORAGE_BUCKET_NAME)

There's also a storage that works well with Django Compressor,
collectstatic command and offline assets compression:

  .. code-block:: py

    STATICFILES_STORAGE = "herokuify.storage.CachedS3StaticStorage"
    STATIC_URL = "https://{0}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)

    COMPRESS_STORAGE = "herokuify.storage.CachedS3StaticStorage"
    COMPRESS_OFFLINE = True


Remember to configure and include :doc:`aws` config in your settings
as well enable user environment variables in the
[Slug compilation](https://devcenter.heroku.com/articles/slug-compiler) build
phase, so the storage backend is able to connect to S3 when executing
``collectstatic`` and ``compress`` commands:

  .. code-block: shell

    heroku labs:enable user-env-compile

.. note::

    `Django on Heroku: installing NodeJS and Less for static assets
    compilation <http://en.ig.ma/notebook/2012/django-heroku-nodejs-and-less-compiling-assets>`_
    and `Django and Heroku Cookbook <https://github.com/nigma/heroku-django-cookbook>`_
    provides more information and build scripts for automatic static files
    compression during deployment.

Available storage backends
--------------------------

S3 Static and Media storage
+++++++++++++++++++++++++++

.. autoclass:: S3StaticStorage

.. autoclass:: S3MediaStorage


Django Compressor-compatible storage
++++++++++++++++++++++++++++++++++++

.. autoclass:: CachedS3BotoStorage

.. autoclass:: CachedS3StaticStorage
