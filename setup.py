#!/usr/bin/env python

from distutils.core import setup

with open('README.md') as f:
    long_description=f.read()

setup(name='pyzmq-wrapper',
      version='0.1.0a',
      description='Wrapper classes for pyzmq',
      long_description=long_description,
      author='Narahari Allamraju',
      author_email='anarahari@gmail.com',
      url='https://github.com/supercoderz/pyzmq-wrapper',
      packages=['zmqwrapper'],
      requires=['pyzmq','pytest'],
     )
