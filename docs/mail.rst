.. _mail:

Email configuration
===================

.. note:: For now the project includes only Mailgun configuration. Feel free to
          contribute definitions for other providers.

Retrieves `Mailgun add-on`_ settings from the environment and predefines:

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
-------------

Import settings from this module into your Django project settings::

    from herokuify.mail.mailgun import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT


Mailgun add-on
--------------

Use ``heroku addons`` command to subscribe for
`Mailgun add-on <https://addons.heroku.com/mailgun>`:

  .. code-block:: shell

    heroku addons:add mailgun:<PLAN>

Quick start with:

  .. code-block:: shell

    heroku addons:add mailgun:starter


Defined model attributes
------------------------

.. automodule:: herokuify.mail.mailgun
   :members:


.. _Mailgun Add-on: https://addons.heroku.com/mailgun
