#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = "1.0.pre2"

setup(
    name="django-herokuify",
    version=version,
    description="Automatic Django configuration and utilities for Heroku.",
    license="BSD",

    author="Filip Wasilewski",
    author_email="en@ig.ma",

    url="https://github.com/nigma/django-herokuify",
    download_url='https://github.com/nigma/django-herokuify/zipball/master',

    long_description=open("README.rst").read(),

    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],

    install_requires=filter(None, open("requirements.txt").read().splitlines())
)
