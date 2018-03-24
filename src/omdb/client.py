"""OMDb API client.
"""

import re

import requests

from ._compat import iteritems, number_types


RE_CAMELCASE = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')


class OMDBClient(object):
    """HTTP request client for OMDb API."""
    url = 'http://www.omdbapi.com'
    params_map = {
        's': 'search',
        't': 'title',
        'i': 'imdbid',
        'y': 'year',
        'page': 'page',
        'Season': 'season',
        'Episode': 'episode',
        'plot': 'plot',
        'type': 'type',
        'tomatoes': 'tomatoes',
        'apikey': 'apikey'
    }

    def __init__(self, **defaults):
        self.default_params = defaults
        self.session = requests.Session()

    def set_default(self, key, default):
        """Set default request params."""
        self.default_params[key] = default

    def request(self, **params):
        """Lower-level HTTP GET request to OMDb API.

        Raises exception for non-200 HTTP status codes.
        """
        timeout = params.pop('timeout', self.default_params.get('timeout'))
        params.setdefault('apikey', self.default_params.get('apikey'))

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
            page=1,
            fullplot=None,
            tomatoes=None,
            media_type=None,
            season=None,
            episode=None,
            timeout=None):
        """Make OMDb API GET request and return results."""
        params = {
            'search': search,
            'title': title,
            'imdbid': imdbid,
            'year': year,
            'page': page,
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
        params = self.format_params(params)

        data = self.request(**params).json()

        return self.format_search_results(data, params)

    def format_params(self, params):
        """Format our custom named params to OMDb API param names."""
        return {api_param: params[param]
                for api_param, param in iteritems(self.params_map)
                if param in params}

    def format_search_results(self, data, params):
        """Format OMDb API search results into standard format."""
        if 's' in params:
            # omdbapi returns search results even if imdbid supplied
            return self.format_search_list(data.get('Search', []))
        else:
            return self.format_search_item(data)

    def format_search_list(self, items):
        """Format each search item using :meth:`format_search_item`."""
        return [self.format_search_item(item) for item in items]

    def format_search_item(self, item):
        """Format search item by converting dict key case from camel case to
        underscore case.
        """
        if not isinstance(item, dict):  # pragma: no cover
            return item

        if 'Error' in item:
            return {}

        return {camelcase_to_underscore(key): (self.format_search_list(value)
                                               if isinstance(value, list)
                                               else value)
                for key, value in iteritems(item)}


def camelcase_to_underscore(string):
    """Convert string from ``CamelCase`` to ``underscore_case``."""
    return RE_CAMELCASE.sub(r'_\1', string).lower()
