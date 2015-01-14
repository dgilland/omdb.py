"""Public interface for omdb module

Accessible via:

    import omdb
"""

from .client import Client

# Internal client instance used for our requests.
_client = Client()


def set_default(key, default):
    """Proxy method to internal client instance that sets default params
    values.
    """
    _client.set_default(key, default)


def get(**params):
    """Generic request."""
    return _client.get(**params)


def search(string, **params):
    """Search by string."""
    return get(search=string, **params)


def search_movie(string, **params):
    """Search movies by string."""
    params['media_type'] = 'movie'
    return search(string, **params)


def search_episode(string, **params):
    """Search episodes by string."""
    params['media_type'] = 'episode'
    return search(string, **params)


def search_series(string, **params):
    """Search series by string."""
    params['media_type'] = 'series'
    return search(string, **params)


def imdbid(string, **params):
    """Get by IMDB ID."""
    return get(imdbid=string, **params)


def title(string, **params):
    """Get by title."""
    return get(title=string, **params)


def request(**params):
    """Lower-level request."""
    return _client.request(**params)
