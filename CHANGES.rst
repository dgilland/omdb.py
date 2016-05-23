Changelog
=========


v0.6.0 (2016-05-22)
-------------------

- Add support for ``timeout`` parameter to all HTTP requests.


v0.5.0 (2015-07-29)
-------------------

- Add support for ``Season``/``Episode`` OMDb parameter via ``season``/``episode`` arguments to every main API function. Thanks cihansahin_!


v0.4.0 (2015-04-29)
-------------------

- Add ``Season``, ``Episode``, and ``SeriesID`` OMDb API fields as ``season``, ``episode``, and ``series_id`` model fields.


v0.3.1 (2015-01-27)
-------------------

- Add metadata to main module:

    - ``__title__``
    - ``__summary__``
    - ``__url__``
    - ``__version__``
    - ``__author__``
    - ``__email__``
    - ``__license__``


v0.3.0 (2015-01-13)
-------------------

- Add ``search_movie``.
- Add ``search_episode``.
- Add ``search_series``.
- Add support for ``type`` OMDb parameter via ``media_type`` argument to every main API function.


v0.2.0 (2014-10-16)
-------------------

- Update ``models.Item`` with additional ``OMDb API`` fields: ``Awards``, ``Country``, ``Language``, and ``Metascore``.
- Add ``omdb.request`` method for easier access to raw request response.
- Initialization of ``omdb.Client`` now accepts keyword arguments for API request parameter defaults. Previously, a ``dict`` object needed to be passed in.
- Full PEP8 compliance.
- Integrate ``tox`` testing into ``setup.py``.


v0.1.1 (2014-02-09)
-------------------

- Python3 support. Thanks agronholm_!
- PEP8 compliance excluding max-line-length. Thanks agronholm_!
- Wheel support. Thanks agronholm_!


v0.1.0 (2013-11-24)
-------------------

- Convert API response to data models (see omdb/models.py).
- Add /tests folder and move appropriate doctests there.
- Return empty data for ``search`` and ``get`` requests which return no record(s).
- Add ``omdb.set_default()`` for setting default request parameters (e.g. ``set_default(tomatoes=True)`` to always include tomatoes data)


v0.0.1 (2013-11-12)
-------------------

- Initial release.


.. _agronholm: https://github.com/agronholm
.. _cihansahin: https://github.com/cihansahin
