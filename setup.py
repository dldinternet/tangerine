#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains setup instructions for tangerine."""
import codecs
import os
import sys
from shutil import rmtree

from setuptools import Command
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()


class UploadCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds ...')
            rmtree(os.path.join(here, 'dist'))
        except Exception:
            pass
        self.status('Building Source distribution ...')
        os.system('{0} setup.py sdist bdist_wheel'.format(sys.executable))
        self.status('Uploading the package to PyPI via Twine ...')
        os.system('twine upload dist/*')
        sys.exit()


setup(
    name='slack-tangerine',
    version='5.0.2',
    author='Nick Ficano',
    author_email='nficano@gmail.com',
    packages=['tangerine'],
    url='https://github.com/nficano/tangerine',
    license='MIT',
    package_data={
        '': ['LICENSE'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    description=(
        'tangerine is a lightweight Slackbot framework that abstracts away '
        'all the boilerplate code required to write bots, allowing you to '
        'focus on the problem at hand.'
    ),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,
    zip_safe=True,
    cmdclass={'upload': UploadCommand},
)
