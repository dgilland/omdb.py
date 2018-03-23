"""OMDb API library.
"""

from .__pkg__ import (
    __description__,
    __url__,
    __version__,
    __author__,
    __email__,
    __license__
)

from .api import (
    Client,
    get,
    imdbid,
    request,
    search,
    search_movie,
    search_episode,
    search_series,
    set_default,
    title,
)
