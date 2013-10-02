# -*- encoding: utf8 -*-
import os
from email.utils import parseaddr
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
<<<<<<< HEAD
author, author_email = parseaddr("Author <email>")  # Edit
=======

author, author_email = parseaddr("Victor Aguilar <jvacx.log@gmail.com>")  # Edit
>>>>>>> 388721d9f09a096cd79494cb9704be926f0f8892
version = "0.1"  # Edit
url = 'http://github.com/jvacx/footesh'  # Edit

setup(name='finish',
    url=url,
    version=version,
    description=README.split('\n\n')[0],
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author=author,
    author_email=author_email,
    packages=find_packages(),
    namespace_packages=['finish'],
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    zip_safe=False,
)
