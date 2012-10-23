.. _db:

Database configuration
======================

Provides :func:`herokuify.db.get_db_config` function that reads PostgreSQL
database settings from Heroku environment.

.. note::

    This functionality relies on `django-heroku-postgresify <https://github.com/rdegges/django-heroku-postgresify>`_.

.. automodule:: herokuify.db
   :members: get_db_config

Django config
-------------

Use this to configure database settings in your Django project:

  .. code-block:: py

    import herokuify
    DATABASES = herokuify.get_db_config()
