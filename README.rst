*******
omdb.py
*******

|version| |travis| |coveralls| |license|

Python wrapper around ``The Open Movie Database API`` (a.k.a. ``OMDb API``): http://omdbapi.com/

**NOTE:** This library and its author are not endorsed by or affiliated with `OMDbAPI.com <http://omdbapi.com/>`_.


Installation
============

Using ``pip``:


::

	pip install omdb


Dependencies
============

- requests >= 2.0.1


API
===

Each ``omdb.py`` method supports the same parameters as the ``OMDb API``.


Paramters
---------

=================  ==================  =======================  ===================================================================
OMDb API Param     omdb.py Param       Value                    Description
=================  ==================  =======================  ===================================================================
``s``              ``search``          string **(optional)**    title of media to search for
``i``              ``imdbid``          string **(optional)**    a valid IMDb ID
``t``              ``title``           string **(optional)**    title of media to return
``y``              ``year``            year **(optional)**      year of media
``Season``         ``season``          season **(optional)**    season number
``Episode``        ``episode``         episode **(optional)**   episode number
``type``           ``media_type``      string **(optional)**    media type to return (one of ``movie``, ``episode``, or ``series``)
``plot=full``      ``fullplot=True``   ``full``                 include extended plot
``plot=short``     ``fullplot=False``  ``short``                include short plot **(default)**
``tomatoes=true``  ``tomatoes=True``   ``true`` **(optional)**  add Rotten Tomatoes data to response
=================  ==================  =======================  ===================================================================

**NOTE:** By default all ``OMDb API`` responses are formatted as ``JSON``. However, ``OMDb API`` also supports responses formatted as ``XML``. Since ``omdb.py`` will handle ``JSON`` to ``dict`` conversion automatically, it's generally not necessary (nor is it supported by the main ``ombd.py`` methods) to return ``XML`` formatted responses. But this can be accomplished by directly using ``omdb.request``:


.. code-block:: python

	import omdb

	# must use OMDb API parameters
	res = omdb.request(t='True Grit', y=1969, r='xml')
	xml_content = res.content


Methods
-------

All methods are accessible via:


.. code-block:: python

	import omdb

	# omdb.<method>

=====================================  =======================================================================================  ==========
Method                                 Description                                                                              Returns
=====================================  =======================================================================================  ==========
``get(**params)``                      Generic request to OMDb API (requires keyword argument passing of all parameters).       ``Item``
``search(search, **params)``           Search by string.                                                                        ``Search``
``search_movie(search, **params)``     Search movies by string.                                                                 ``Search``
``search_episode(search, **params)``   Search episodes by string.                                                               ``Search``
``search_series(search, **params)``    Search series by string.                                                                 ``Search``
``imdbid(imdbid, **params)``           Get by IMDB ID                                                                           ``Item``
``title(title, **params)``             Get by title                                                                             ``Item``
``set_default(key, default)``          Set default request parameter                                                            ``None``
=====================================  =======================================================================================  ==========


Client
------

While generally not necessary, one can use the lower level ``OMDb API Client`` for accessing the API:


.. code-block:: python

    from omdb import Client

    client = Client()

=============================  =========================================================================================  =========================
Class Methods                  Description                                                                                Returns
=============================  =========================================================================================  =========================
``get(**omdb_params)``         Generic request to OMDb API which can be used for any type of query.                       ``Search`` or ``GetItem``
``request(**omdbapi_params)``  Lower-level request to OMDb API which accepts URL query parameters supported by OMDb API.  ``request.Response``
``set_default(key, default)``  Set default request parameter.                                                             ``None``
=============================  =========================================================================================  =========================


Models
------

Movie data returned from the ``OMDb API`` is converted to a custom dict subclass which allows both ``data['key']`` and ``data.key`` access.

There are two main models:

- ``omdb.models.Search`` (a list of ``Item`` instances)
- ``omdb.models.Item``

Which can be accessed like the following:


.. code-block:: python

	import omdb

	movie = omdb.title('True Grit')
	movie.title == 'True Grit'
	movie['title'] == 'True Grit'

	search = omdb.search('True Grit')
	search[0].title == 'True Grit'


All fields from the ``OMDb API`` are converted from ``CamelCaseFields`` to ``underscore_fields``:


Search Model Fields
~~~~~~~~~~~~~~~~~~~

==============  =============
OMDb API Field  omdb.py Field
==============  =============
``Title``       ``title``
``Year``        ``year``
``Type``        ``type``
``imdbID``      ``imdb_id``
==============  =============


Get Model Fields (tomatoes=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==============  ===============
OMDb API Field  omdb.py Field
==============  ===============
``Title``       ``title``
``Year``        ``year``
``Type``        ``type``
``Actors``      ``actors``
``Awards``      ``awards``
``Country``     ``country``
``Director``    ``director``
``Genre``       ``genre``
``Episode``     ``episode``
``Season``      ``season``
``SeriesID``    ``series_id``
``Language``    ``language``
``Metascore``   ``metascore``
``Plot``        ``plot``
``Poster``      ``poster``
``Rated``       ``rated``
``Released``    ``released``
``Response``    ``response``
``Runtime``     ``runtime``
``Writer``      ``writer``
``imdbID``      ``imdb_id``
``imdbRating``  ``imdb_rating``
``imdbVotes``   ``imdb_votes``
==============  ===============


Get Model Fields (tomatoes=True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=====================  =======================
OMDb API Field         omdb.py Field
=====================  =======================
``Title``              ``title``
``Year``               ``year``
``Type``               ``type``
``Actors``             ``actors``
``Awards``             ``awards``
``Country``            ``country``
``Director``           ``director``
``Genre``              ``genre``
``Episode``            ``episode``
``Season``             ``season``
``SeriesID``           ``series_id``
``Language``           ``language``
``Metascore``          ``metascore``
``Plot``               ``plot``
``Poster``             ``poster``
``Rated``              ``rated``
``Released``           ``released``
``Runtime``            ``runtime``
``Writer``             ``writer``
``imdbID``             ``imdb_id``
``imdbRating``         ``imdb_rating``
``imdbVotes``          ``imdb_votes``
``BoxOffice``          ``box_office``
``DVD``                ``dvd``
``Production``         ``production``
``Website``            ``website``
``tomatoConsensus``    ``tomato_consensus``
``tomatoFresh``        ``tomato_fresh``
``tomatoImage``        ``tomato_image``
``tomatoMeter``        ``tomato_meter``
``tomatoRating``       ``tomato_rating``
``tomatoReviews``      ``tomato_reviews``
``tomatoRotten``       ``tomato_rotten``
``tomatoUserMeter``    ``tomato_user_meter``
``tomatoUserRating``   ``tomato_user_rating``
``tomatoUserReviews``  ``tomato_user_reviews``
=====================  =======================


Usage
=====


General Import
--------------


.. code-block:: python

	import omdb


.. note::

    All functions below support a ``timeout`` keyword argument that will be forwarded to the underlying ``requests.get`` function call. You can also set a global default using ``omdb.set_default('timeout', <timeout>)`` that will be used when ``timeout`` is not explicitly provided.


omdb.get()
----------


.. code-block:: python

	# include full plot and Rotten Tomatoes data
	omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True)

	# set timeout of 5 seconds for this request
	omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True, timeout=5)


omdb.search()
-------------


.. code-block:: python

	# search by string
	omdb.search('True Grit')
	omdb.search('True Grit', timeout=5)


omdb.search_movie()
-------------------


.. code-block:: python

	# search movies by string
	omdb.search_movie('True Grit')
	omdb.search_movie('True Grit', timeout=5)


omdb.search_episode()
---------------------


.. code-block:: python

	# search episodes by string
	omdb.search_episode('True Grit')
	omdb.search_episode('True Grit', timeout=5)


omdb.search_series()
--------------------


.. code-block:: python

	# search series by string
	omdb.search_series('True Grit')
	omdb.search_series('True Grit', timeout=5)


omdb.imdbid()
-------------


.. code-block:: python

	# get by IMDB id
	omdb.imdbid('tt0065126')
	omdb.imdbid('tt0065126', timeout=5)


omdb.title()
------------


.. code-block:: python

	# get by title
	omdb.title('True Grit')
	omdb.title('True Grit', timeout=5)


omdb.set_default()
------------------


.. code-block:: python

	# include tomatoes data by default
	omdb.set_default('tomatoes', True)
	omdb.title('True Grit') == omdb.title('True Grit', tomatoes=True)

	# set a global timeout of 5 seconds for all HTTP requests
	omdb.set_default('timeout', 5)


omdb.request()
--------------


.. code-block:: python

	# lower level API request
	omdb.request(t='True Grit', y=1969, plot='full', tomatoes='true', timeout=5)


**Returns:**

A ``requests.Response`` object.


Errors and Exceptions
=====================

Under the hood, ``omdb.py`` uses the `requests <http://www.python-requests.org/>`_ library. For a listing of explicit exceptions raised by ``requests``, see `Requests: Errors and Exceptions <http://www.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions>`_.

By default ``requests`` will not raise an ``Exception`` when an HTTP response's status code is not ``200``. However, ``omdb.py`` *WILL* raise an ``requests.exceptions.HTTPError`` error for any response with a non-200 status code.


.. |version| image:: http://img.shields.io/pypi/v/omdb.svg?style=flat-square
    :target: https://pypi.python.org/pypi/omdb

.. |travis| image:: http://img.shields.io/travis/dgilland/omdb.py/master.svg?style=flat-square
    :target: https://travis-ci.org/dgilland/omdb.py

.. |coveralls| image:: http://img.shields.io/coveralls/dgilland/omdb.py/master.svg?style=flat-square
    :target: https://coveralls.io/r/dgilland/omdb.py

.. |license| image:: http://img.shields.io/pypi/l/omdb.svg?style=flat-square
    :target: https://pypi.python.org/pypi/omdb
