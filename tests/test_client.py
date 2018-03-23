
import pytest
from requests.exceptions import Timeout

import omdb


def test_request(client):
    req = {'t': 'True Grit', 'y': '1969'}
    res = client.request(**req)

    assert res.ok

    data = res.json()

    assert data['Title'] == req['t']
    assert data['Year'] == req['y']


def test_get(client):
    req = {'title': 'True Grit',
           'year': '1969',
           'fullplot': True,
           'tomatoes': True}
    data = client.get(**req)

    assert data['title'] == req['title']
    assert data['year'] == req['year']
    assert 'tomato_meter' in data


def test_set_default(client):
    req = {'title': 'True Grit'}

    data = client.get(**req)

    # default request returns movie with this year
    assert data['year'] == '2010'

    # change the default year and re-request
    client.set_default('year', '1969')

    data = client.get(**req)

    # default year is now used
    assert data['year'] == '1969'

    # can also set defaults at client instantiation time
    client = omdb.OMDBClient(year='1969',
                             apikey=client.default_params['apikey'])

    data = client.get(**req)

    assert data['year'] == '1969'

    # defaults can be overridden
    req = {'title': 'True Grit', 'year': '2010'}
    data = client.get(**req)

    assert data['year'] == '2010'
