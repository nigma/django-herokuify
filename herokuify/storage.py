#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.files.storage import get_storage_class

from storages.backends.s3boto import S3BotoStorage


class S3StaticStorage(S3BotoStorage):
    """
    Subclasses :class:`storages.backends.s3boto.S3BotoStorage` and
    sets base location for files to ``/static``.
    """
    def __init__(self, *args, **kwargs):
        kwargs["location"] = "static"
        super(S3StaticStorage, self).__init__(*args, **kwargs)


class S3MediaStorage(S3BotoStorage):
    """
    Subclasses :class:`storages.backends.s3boto.S3BotoStorage` and
    sets base location for files to ``/media``.
    """
    def __init__(self, *args, **kwargs):
        kwargs["location"] = "media"
        super(S3MediaStorage, self).__init__(*args, **kwargs)


class CachedS3BotoStorage(S3BotoStorage):
    """
    S3 storage backend that saves the files both remotely and locally.

    See http://django_compressor.readthedocs.org/en/latest/remote-storages/
    """
    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name


class CachedS3StaticStorage(CachedS3BotoStorage):
    """
    Mix of the :class:`S3MediaStorage` and :class:`CachedS3BotoStorage`,
    saves files in ``/static`` subdirectory
    """
    def __init__(self, *args, **kwargs):
        kwargs["location"] = "static"
        super(CachedS3StaticStorage, self).__init__(*args, **kwargs)
