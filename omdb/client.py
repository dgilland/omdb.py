"""OMDb API client.
"""

import requests

from . import models
from ._compat import iteritems, number_types


class Client(object):
    """HTTP request client for OMDB API."""

    url = 'http://www.omdbapi.com'

    params_map = {
        's': 'search',
        't': 'title',
        'i': 'imdbid',
        'y': 'year',
        'Season': 'season',
        'Episode': 'episode',
        'plot': 'plot',
        'type': 'type',
        'tomatoes': 'tomatoes'
    }

    def __init__(self, **defaults):
        self.default_params = defaults
        self.session = requests.Session()

    def set_default(self, key, default):
        """Set default request params."""
        self.default_params[key] = default

    def convert_params(self, params):
        """Map OMDb params to our renaming."""
        new_params = params.copy()

        for api_arg, arg in iteritems(self.params_map):
            if arg in params:
                new_params[api_arg] = new_params.pop(arg)

        return new_params

    def request(self, **params):
        """HTTP GET request to OMDB API.

        Raises exception for non-200 HTTP status codes.
        """
        if 'timeout' in params:
            timeout = params.pop('timeout')
        else:
            timeout = self.default_params.get('timeout')

        res = self.session.get(self.url, params=params, timeout=timeout)

        # raise HTTP status code exception if status code != 200
        # if status_code == 200, then no exception raised
        res.raise_for_status()

        return res

    def get(self,
            search=None,
            title=None,
            imdbid=None,
            year=None,
            fullplot=None,
            tomatoes=None,
            media_type=None,
            season=None,
            episode=None,
            timeout=None):
        """Generic request returned as dict."""

        params = {
            'search': search,
            'title': title,
            'imdbid': imdbid,
            'year': year,
            'type': media_type,
            'plot': 'full' if fullplot else 'short',
            'tomatoes': 'true' if tomatoes else False,
            'season': season,
            'episode': episode,
            'timeout': timeout
        }

        # remove falsey params
        params = dict([(key, value) for key, value in iteritems(params)
                       if value or isinstance(value, number_types)])

        # set defaults
        for key in self.params_map.values():
            if key in self.default_params:
                params.setdefault(key, self.default_params[key])

        # convert function args to API query params
        params = self.convert_params(params)

        data = self.request(**params).json()

        return self.set_model(data, params)

    def set_model(self, data, params):  # pylint: disable=no-self-use
        """Convert data into first class models."""
        if 's' in params:
            # omdbapi returns search results even if imdbid supplied
            data = models.Search(data)
        else:
            data = models.Item(data)

        return data
