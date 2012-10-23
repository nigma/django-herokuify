#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

__all__ = [
    "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_STORAGE_BUCKET_NAME"
]

#: AWS access key id retrieved from ``AWS_ACCESS_KEY_ID`` environment setting
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

#: AWS secret key retrieved from ``AWS_SECRET_ACCESS_KEY`` environment setting
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

#: AWS S3 bucket name retrieved from ``AWS_STORAGE_BUCKET_NAME`` environment setting
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
