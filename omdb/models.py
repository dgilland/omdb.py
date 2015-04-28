"""OMDb models.
"""

import re


class Storage(dict):
    """An object that is like a dict except `obj.foo` can be used in addition
    to `obj['foo']`.

    Raises Attribute/Key errors for missing references.

    >>> o = Storage(a=1, b=2)

    >>> assert o.a == o['a']
    >>> assert o.b == o['b']

    >>> o.a = 2
    >>> print(o['a'])
    2

    >>> x = o.copy()
    >>> assert(x == o)

    >>> del o.a
    >>> print(o.a)
    Traceback (most recent call last):
    ...
    AttributeError: a

    >>> del o.a
    Traceback (most recent call last):
    ...
    AttributeError: a

    >>> print(o['a'])
    Traceback (most recent call last):
    ...
    KeyError: 'a'
    """

    def __getattr__(self, key):
        if key in self:
            return self[key]
        else:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        if key in self:
            del self[key]
        else:
            raise AttributeError(key)

    def __repr__(self):  # pragma: no cover
        return '%s(%s)' % (self.__class__.__name__, dict.__repr__(self))


class Item(Storage):
    """Data model for an individual OMDb item."""
    _fields = [
        'Actors',
        'Awards',
        'BoxOffice',
        'Country',
        'DVD',
        'Director',
        'Episode',
        'Genre',
        'Language',
        'Metascore',
        'Plot',
        'Poster',
        'Production',
        'Rated',
        'Released',
        'Response',
        'Runtime',
        'Season',
        'seriesID',
        'Title',
        'Type',
        'Website',
        'Writer',
        'Year',
        'imdbID',
        'imdbRating',
        'imdbVotes',
        'tomatoConsensus',
        'tomatoFresh',
        'tomatoImage',
        'tomatoMeter',
        'tomatoRating',
        'tomatoReviews',
        'tomatoRotten',
        'tomatoUserMeter',
        'tomatoUserRating',
        'tomatoUserReviews'
    ]

    def __init__(self, data_dict=None, **data):
        # pylint: disable=super-init-not-called
        data = data_dict or data

        if 'Error' not in data:
            for field in self._fields:
                if field in data:
                    self[camelcase_to_underscore(field)] = data[field]


class Search(list):
    """Data model for an OMDb search."""
    def __init__(self, results):
        # pylint: disable=super-init-not-called
        # If 'Search' not present, then no results found. Currently, api
        # returns {u'Response': u'False', u'Error': u'Movie not found!'} when
        # no results.
        self.extend(results.get('Search', []))

        for i, item in enumerate(self):
            self[i] = Item(item)

    def __repr__(self):  # pragma: no cover
        return 'Search(%s)' % (super(Search, self).__repr__())


def camelcase_to_underscore(string):
    """Convert string from ``CamelCase`` to ``under_score``."""
    return (re.sub('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))', r'_\1', string)
            .lower())
