
import requests

class Client(object):
    '''HTTP request client for OMDB API'''

    url = 'http://www.omdbapi.com'

    @classmethod
    def request(cls, **params):
        '''
        HTTP GET request to OMDB API

        Raises exception for non-200 HTTP status codes

        >>> req = dict(t='True Grit', y='1969')
        >>> res = Client.request(**req)
        >>> assert res.ok

        >>> data = res.json()
        >>> assert data['Title'] == req['t']
        >>> assert data['Year'] == req['y']
        '''
        res = requests.get(cls.url, params=params)

        # raise HTTP status code exception if status code != 200
        # if status_code == 200, then no exception raised
        res.raise_for_status()

        return res

    @classmethod
    def get(cls, search=None, title=None, imdbid=None, year=None, fullplot=None, tomatoes=None, **ignore):
        '''
        Generic request returned as dict

        >>> req = dict(title='True Grit', year='1969', fullplot=True, tomatoes=True)
        >>> data = Client.get(**req)
        >>> assert data['Title'] == req['title']
        >>> assert data['Year'] == req['year']
        >>> assert 'tomatoMeter' in data
        '''

        # convert function args to API query params
        params = dict(
            s = search,
            t = title,
            i = imdbid,
            y = year,
            plot = 'full' if fullplot else 'short',
            tomatoes = 'true' if tomatoes else False
        )

        # remove falsey params
        params = dict([(k,v) for k,v in params.iteritems() if v])

        return cls.request(**params).json()

