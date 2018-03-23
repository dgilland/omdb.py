
import os

import pytest

import omdb


def pytest_sessionstart(session):
    apikey = os.getenv('OMDBAPIKEY')

    if not apikey:
        try:
            with open('omdbapikey') as fp:
                apikey = fp.read().strip()
        except FileNotFoundError:
            pass

    if not apikey:
        pytest.exit('ERROR: OMDb API key not found. Cannot continue test run. '
                    'Set API key value either in the environment variable '
                    '"OMDB_APIKEY" or in the file "omdbapikey" in root of '
                    'project.')

    session.config.cache.set('omdbapikey', apikey)


@pytest.fixture(autouse=True)
def apikey(cache):
    omdb.set_default('apikey', cache.get('omdbapikey', None))
    yield
    omdb.set_default('apikey', None)


@pytest.fixture(autouse=True)
def omdb_defaults():
    orig_defaults = omdb.api._client.default_params.copy()
    yield
    omdb.api._client.default_params = orig_defaults


@pytest.fixture
def client(cache):
    return omdb.OMDBClient(apikey=cache.get('omdbapikey', None))
