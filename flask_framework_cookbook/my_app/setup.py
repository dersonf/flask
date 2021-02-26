#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
import os
from setuptools import setup

setup(
    name = 'my_app',
    version = '1.0',
    license = 'GNU General Public License v3',
    author = 'Shalb Aggarwall',
    author_email = 'contact@shalabhaggarwal.com', 
    description = 'Hello world application for Flask', 
    packages = ['my_app'], 
    platforms = 'any', 
    install_requires = [ 
        'flask', 
    ], 
    classifiers = [ 
        'Development Status :: 4 - Beta', 
        'Environment :: Web Environment', 
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: GNU General Public License v3', 
        'Operating System :: OS Independent', 
        'Programming Language :: Python', 
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content', 
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], 
) 
