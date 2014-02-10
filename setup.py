"""
omdb
----

Python wrapper for OMDbAPI.com.

Documentation: https://github.com/dgilland/omdb.py
"""

from setuptools import setup

setup(
    name='omdb',
    version='0.1.1',
    description='Python wrapper for OMDb API: http://www.omdbapi.com/',
    long_description=__doc__,
    author='Derrick Gilland',
    author_email='dgilland@gmail.com',
    url='https://github.com/dgilland/omdb.py',
    packages=['omdb'],
    install_requires=['requests>=2.0.1', 'six'],
    test_suite='tests',
    keywords='omdb imdb movies',
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
)
