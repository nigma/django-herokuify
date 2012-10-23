.. _aws:

Amazon AWS settings
===================

Reads common AWS settings like ``AWS_ACCESS_KEY_ID``, ``AWS_SECRET_ACCESS_KEY``
and ``AWS_STORAGE_BUCKET_NAME`` from Heroku environment.


Django config
-------------

Simply import settings from this module into your Django project settings file:

  .. code-block:: py

    from herokuify.aws import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME


Heroku config
-------------

Use ``heroku config`` command to define the values:

  .. code-block:: bash

    heroku config:add AWS_ACCESS_KEY_ID=<key id>
    heroku config:add AWS_SECRET_ACCESS_KEY=<secret key>
    heroku config:add AWS_STORAGE_BUCKET_NAME=<bucket name>


Defined model attributes
------------------------

.. automodule:: herokuify.aws
   :members:
