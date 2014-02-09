'''
Public interface for omdb module

Accessible via:

    import omdb
'''

from .client import Client

# internal client instance used for our requests
_client = Client()


def set_default(key, default):
    '''
    Proxy method to internal client instance that sets default params values
    '''
    _client.set_default(key, default)


def get(**params):
    '''Generic request'''
    return _client.get(**params)


def search(search, **params):
    '''
    Search by string
    '''
    return get(search=search, **params)


def imdbid(imdbid, **params):
    '''
    Get by IMDB ID
    '''
    return get(imdbid=imdbid, **params)


def title(title, **params):
    '''
    Get by title
    '''
    return get(title=title, **params)
