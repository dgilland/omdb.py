import requests
import six

from omdb import models


class Client(object):
    '''HTTP request client for OMDB API'''

    url = 'http://www.omdbapi.com'

    default_params = {}

    params_map = {
        's':        'search',
        't':        'title',
        'i':        'imdbid',
        'y':        'year',
        'plot':     'plot',
        'tomatoes': 'tomatoes'
    }

    def __init__(self, default_params=None):
        self.default_params = default_params.copy() if isinstance(default_params, dict) else {}

        self.s = requests.Session()

    def set_default(self, key, default):
        '''
        Set default request params
        '''
        self.default_params[key] = default

    def convert_params(self, params):
        _params = {}

        for api_arg, arg in six.iteritems(self.params_map):
            if arg in params:
                _params[api_arg] = params[arg]

        return _params

    def request(self, **params):
        '''
        HTTP GET request to OMDB API

        Raises exception for non-200 HTTP status codes
        '''
        res = self.s.get(self.url, params=params)

        # raise HTTP status code exception if status code != 200
        # if status_code == 200, then no exception raised
        res.raise_for_status()

        return res

    def get(self, search=None, title=None, imdbid=None, year=None, fullplot=None, tomatoes=None, **ignore):
        '''
        Generic request returned as dict
        '''

        params = dict(
            search=search,
            title=title,
            imdbid=imdbid,
            year=year,
            plot='full' if fullplot else 'short',
            tomatoes='true' if tomatoes else False
        )

        # remove falsey params
        params = dict([(k, v) for k, v in six.iteritems(params) if v])

        # set defaults
        for k, v in six.iteritems(self.default_params):
            params.setdefault(k, v)

        # convert function args to API query params
        params = self.convert_params(params)

        data = self.request(**params).json()

        return self.set_model(data, params)

    def set_model(self, data, params):
        if 's' in params:
            # omdbapi returns search results even if imdbid supplied
            data = models.Search(data)
        else:
            data = models.Item(data)

        return data
