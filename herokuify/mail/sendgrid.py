#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

__all__ = [
    "SENDGRID_SMTP_SERVER", "SENDGRID_USERNAME", "SENDGRID_PASSWORD",
    "SENDGRID_SMTP_PORT",
    "EMAIL_HOST", "EMAIL_HOST_USER", "EMAIL_HOST_PASSWORD", "EMAIL_PORT",
    "EMAIL_USE_TLS"
]

#: Sendgrid SMTP server host
SENDGRID_SMTP_SERVER = "smtp.sendgrid.net"

#: Sendgrid SMTP server login
SENDGRID_USERNAME = os.environ.get("SENDGRID_USERNAME")

#: Sendgrid SMTP server password
SENDGRID_PASSWORD = os.environ.get("SENDGRID_PASSWORD")

#: Sendgrid SMTP server port
SENDGRID_SMTP_PORT = 587

#: Email host for sending mail
EMAIL_HOST = SENDGRID_SMTP_SERVER

#: Email server username
EMAIL_HOST_USER = SENDGRID_USERNAME

#: Email server password
EMAIL_HOST_PASSWORD = SENDGRID_PASSWORD

#: Email server SMTP port
EMAIL_PORT = SENDGRID_SMTP_PORT

#: Email server TLS secure connection
EMAIL_USE_TLS = True
