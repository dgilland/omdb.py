import re


class Storage(dict):
    '''
    An object that is like a dict except `obj.foo` can be used in addition to `obj['foo']`.

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
    '''

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

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, dict.__repr__(self))  # pragma: no cover


class Item(Storage):
    '''
    Data model for an individual OMDb item
    '''
    _fields = [
        'Actors',
        'BoxOffice',
        'DVD',
        'Director',
        'Genre',
        'Plot',
        'Poster',
        'Production',
        'Rated',
        'Released',
        'Runtime',
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
        data = data_dict or data

        if 'Error' not in data:
            for field in self._fields:
                if field in data:
                    self[self.convert_field_name(field)] = data[field]

    def convert_field_name(self, name):
        '''
        Convert field name from CamelCase to camel_case

        >>> item = Item()
        >>> assert item.convert_field_name('CamelCase') == 'camel_case'
        >>> assert item.convert_field_name('imdbId') == 'imdb_id'
        '''
        first_cap_re = re.compile('(.)([A-Z][a-z]+)')
        all_cap_re = re.compile('([a-z0-9])([A-Z])')
        s1 = first_cap_re.sub(r'\1_\2', name)
        return all_cap_re.sub(r'\1_\2', s1).lower()


class Search(list):
    '''
    Data model for an OMDb search
    '''
    def __init__(self, results):
        # if 'Search' not present, then no results found
        # currently, api returns {u'Response': u'False', u'Error': u'Movie not found!'} when no results
        self.extend(results.get('Search', []))

        for i, item in enumerate(self):
            self[i] = Item(item)

    def __repr__(self):
        return 'Search(%s)' % (super(Search, self).__repr__())  # pragma: no cover
