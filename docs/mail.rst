.. _mail:

Email configuration
===================

.. note:: For now the project includes only Mailgun and Sendgrid configuration.
          Feel free to contribute definitions for other providers.

Mailgun add-on
--------------

Retrieves `Mailgun add-on`_ settings from the environment and defines the following
variables in the :mod:`herokuify.mail.mailgun` module:

  - ``MAILGUN_API_KEY``
  - ``MAILGUN_SMTP_SERVER``
  - ``MAILGUN_SMTP_LOGIN``
  - ``MAILGUN_SMTP_PASSWORD``
  - ``MAILGUN_SMTP_PORT``

as well as ``EMAIL_*`` settings for use in Django config:

  - ``EMAIL_HOST``
  - ``EMAIL_HOST_USER``
  - ``EMAIL_HOST_PASSWORD``
  - ``EMAIL_PORT``

Django config
~~~~~~~~~~~~~

Import settings from this module into your Django project settings::

    from herokuify.mail.mailgun import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT

Installing add-on
~~~~~~~~~~~~~~~~~

Use ``heroku addons`` command to subscribe for
`Mailgun add-on <https://addons.heroku.com/mailgun>`_:

  .. code-block:: bash

    heroku addons:add mailgun:<PLAN>

Quick start with:

  .. code-block:: bash

    heroku addons:add mailgun:starter


Sendgrid add-on
---------------

Retrieves `Sendgrid add-on`_ settings from the environment and defines the following
variables in the :mod:`herokuify.mail.sendgrid` module:

  - ``SENDGRID_SMTP_SERVER``
  - ``SENDGRID_USERNAME``
  - ``SENDGRID_PASSWORD``
  - ``SENDGRID_SMTP_PORT``

as well as ``EMAIL_*`` settings for use in Django config:

  - ``EMAIL_HOST``
  - ``EMAIL_HOST_USER``
  - ``EMAIL_HOST_PASSWORD``
  - ``EMAIL_PORT``
  - ``EMAIL_USE_TLS``

Django config
~~~~~~~~~~~~~

Import settings from this module into your Django project settings::

    from herokuify.mail.sendgrid import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS

Installing add-on
~~~~~~~~~~~~~~~~~

See `Sendgrid add-on page <https://addons.heroku.com/sendgrid>`_. Quick start with:

  .. code-block:: bash

    heroku addons:add sendgrid:starter


Defined module attributes
-------------------------

Mailgun
~~~~~~~

.. automodule:: herokuify.mail.mailgun
   :members:

Sendgrid
~~~~~~~~

.. automodule:: herokuify.mail.sendgrid
   :members:


.. _Mailgun Add-on: https://addons.heroku.com/mailgun
.. _Sendgrid Add-on: https://addons.heroku.com/sendgrid
