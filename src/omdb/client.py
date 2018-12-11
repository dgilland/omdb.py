"""OMDb API client.
"""

import itertools
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
        'type': 'media_type',
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
        params.setdefault('apikey', self.default_params.get('apikey'))
        timeout = params.pop('timeout', None)

        if timeout is None and 'timeout' in self.default_params:
            timeout = self.default_params['timeout']

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
        args = dict(
            search=search,
            title=title,
            imdbid=imdbid,
            year=year,
            page=page,
            fullplot=fullplot,
            tomatoes=tomatoes,
            media_type=media_type,
            season=season,
            episode=episode,
        )

        params = {
            key: value for key, value in itertools.chain(
                iteritems(self.default_params),
                iteritems(args)
            )
            if (
                key in args and
                value is not None and
                (value or isinstance(value, number_types))
            )
        }

        # handle special cases
        params['plot'] = 'full' if params.pop('fullplot', None) else 'short'

        if params.get('tomatoes'):
            params['tomatoes'] = 'true'

        # convert function args to API query params
        params = self.format_params(params)

        data = self.request(timeout=timeout, **params).json()

        return self.format_search_results(data, params)

    def search(self, string, **params):
        """Search by string."""
        return self.get(search=string, **params)

    def search_movie(self, string, **params):
        """Search movies by string."""
        params['media_type'] = 'movie'
        return self.search(string, **params)

    def search_episode(self, string, **params):
        """Search episodes by string."""
        params['media_type'] = 'episode'
        return self.search(string, **params)

    def search_series(self, string, **params):
        """Search series by string."""
        params['media_type'] = 'series'
        return self.search(string, **params)

    def imdbid(self, string, **params):
        """Get by IMDB ID."""
        return self.get(imdbid=string, **params)

    def title(self, string, **params):
        """Get by title."""
        return self.get(title=string, **params)

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
