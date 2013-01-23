.. _cache:

Cache
=====

Provides :func:`herokuify.cache.get_cache_config` that reads Memcache cache
settings from Heroku environment for `Memcache <https://addons.heroku.com/memcache>`_
or `MemCachier <https://addons.heroku.com/memcachier>`_ add-ons.

.. note::

    This functionality relies on `django-heroku-memcacheify <https://github.com/rdegges/django-heroku-memcacheify>`_.

.. automodule:: herokuify.cache
   :members: get_cache_config

Django config
-------------

Use this to configure cache settings in your Django project:

  .. code-block:: py

    import herokuify
    CACHES = herokuify.get_cache_config()

Heroku config
-------------

Use ``heroku addons`` command to subscribe for
`Memcache <https://addons.heroku.com/memcache>`_
or `MemCachier <https://addons.heroku.com/memcachier>`_.

Quick start with either:

  .. code-block:: bash

    heroku addons:add memcache:5mb

    heroku addons:add memcachier:dev
