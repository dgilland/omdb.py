
from setuptools import setup
import os

with open('VERSION', 'r') as f:
    version = f.read()

# load README as long description
with open('README', 'r') as f:
    long_description = f.read()

setup(
    name                = 'omdb',
    version             = version,
    description         = 'Python wrapper for OMDb API: http://www.omdbapi.com/',
    long_description    = long_description,
    author              = 'Derrick Gilland',
    author_email        = 'dgilland@gmail.com',
    url                 = 'https://github.com/dgilland/omdb.py',
    packages            = ['omdb'],
    install_requires    = ['requests>=2.0.1'],
    keywords            = 'omdb imdb movies',
    license             = 'BSD',
    classifiers         = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License'
    ]
)
