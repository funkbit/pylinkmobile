#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from linkmobile import __version__

def publish():
    """Publish to Pypi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(name='pylinkmobile',
      version=__version__,
      description='Link Mobile Solutions API wrapper',
      long_description=open('README.md').read(),
      author='Funkbit',
      author_email='post@funkbit.no',
      url='https://github.com/funkbit/pylinkmobile',
      packages=['linkmobile'],
      license='BSD',
      test_suite='tests',
      classifiers = (
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        )
     )
