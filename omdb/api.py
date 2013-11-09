'''
Public interface for omdb module

Accessible via:

    import omdb
'''

from .client import Client

def get(**params):
    '''Generic request'''
    return Client.get(**params)

def search(search, **params):
    '''
    Search by string

    >>> s = 'True Grit'
    >>> data = search(s)
    >>> assert data['Search'][0]['Title'] == 'True Grit'
    '''
    return get(search=search, **params)

def imdbid(imdbid, **params):
    '''
    Get by IMDB ID

    >>> i = 'tt0065126'
    >>> data = imdbid(i)
    >>> assert data['Title'] == 'True Grit'
    '''
    return get(imdbid=imdbid, **params)

def title(title, **params):
    '''
    Get by title

    >>> t = 'True Grit'
    >>> data = title(t)
    >>> assert data['Title'] == 'True Grit'
    '''
    return get(title=title, **params)
