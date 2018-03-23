
import pytest

import omdb


def test_search():
    s = 'True Grit'
    results = omdb.search(s)

    assert results[0]['title'] == s


def test_imdbid():
    i = 'tt0065126'
    result = omdb.imdbid(i)

    assert result['imdb_id'] == i


def test_title():
    t = 'True Grit'
    result = omdb.title(t)

    assert result['title'] == t


def test_search_movie():
    t = 'True Grit'
    media_type = 'movie'

    results = omdb.search_movie(t)
    assert results[0]['type'] == media_type

    result = omdb.get(title=t, media_type=media_type)
    assert result['type'] == media_type


def test_search_series():
    t = 'True Grit'
    media_type = 'series'

    results = omdb.search_series(t)
    assert results[0]['type'] == media_type

    result = omdb.get(title=t, media_type=media_type)
    assert result['type'] == media_type


def test_search_episode():
    t = 'Pilot'
    media_type = 'episode'

    results = omdb.search_episode(t)

    # FIXME: OMDb API is no longer returning results for this query. Have
    # been unable to find an actual type=episode query that returns
    # results. Skip test if no results found until a replacement query can
    # be found.
    if results:
        assert results[0]['type'] == media_type
        assert omdb.get(title=t, media_type=media_type)['type'] == media_type


@pytest.mark.usefixtures('omdb_defaults')
def test_set_default():
    t = 'True Grit'

    result = omdb.title(t)
    assert result['year'] == '2010'

    omdb.set_default('year', '1969')

    result = omdb.title(t)
    assert result['year'] == '1969'


def test_get():
    result = omdb.get(title='True Grit')
    assert result['title'] == 'True Grit'

    result = omdb.get(imdbid='tt0065126')
    assert result['imdb_id'] == 'tt0065126'

    results = omdb.get(search='True Grit')
    assert results[0]['title'] == 'True Grit'


def test_get_season_episode():
    result = omdb.get(title='Breaking Bad', season=1, episode=1)
    assert result['title'] == 'Pilot'


def test_request():
    res = omdb.request(t='True Grit')
    assert res.json()['Title'] == 'True Grit'

    res = omdb.request(i='tt0065126')
    assert res.json()['imdbID'] == 'tt0065126'

    res = omdb.request(s='True Grit')
    assert res.json()['Search'][0]['Title'] == 'True Grit'


def test_empty_data():
    invalid = 'asdfghjkl'

    assert omdb.search(invalid) == []
    assert omdb.title(invalid) == {}
    assert omdb.imdbid(invalid) == {}


def test_search_model_fields():
    expected_fields = [
        'title',
        'year',
        'type',
        'imdb_id',
        'poster'
    ]

    for result in omdb.search('True Grit'):
        assert set(result.keys()) == set(expected_fields)


def test_get_fields():
    expected_fields = [
        'actors',
        'awards',
        'box_office',
        'country',
        'director',
        'dvd',
        'genre',
        'language',
        'metascore',
        'plot',
        'poster',
        'production',
        'rated',
        'ratings',
        'released',
        'response',
        'runtime',
        'title',
        'type',
        'website',
        'writer',
        'year',
        'imdb_id',
        'imdb_rating',
        'imdb_votes'
    ]

    result = omdb.title('True Grit')
    assert set(result.keys()) == set(expected_fields)

    result = omdb.imdbid('tt0065126')
    assert set(result.keys()) == set(expected_fields)


def test_get_series_fields():
    expected_fields = [
        'actors',
        'awards',
        'country',
        'director',
        'episode',
        'genre',
        'language',
        'metascore',
        'plot',
        'poster',
        'season',
        'series_id',
        'rated',
        'ratings',
        'released',
        'response',
        'runtime',
        'title',
        'type',
        'writer',
        'year',
        'imdb_id',
        'imdb_rating',
        'imdb_votes'
    ]

    result = omdb.imdbid('tt2400770')
    assert set(result.keys()) == set(expected_fields)


def test_get_tomatoes_fields():
    expected_fields = [
        'actors',
        'awards',
        'box_office',
        'country',
        'director',
        'dvd',
        'genre',
        'language',
        'metascore',
        'plot',
        'poster',
        'production',
        'rated',
        'ratings',
        'released',
        'response',
        'runtime',
        'title',
        'type',
        'website',
        'writer',
        'year',
        'imdb_id',
        'imdb_rating',
        'imdb_votes',
        'tomato_consensus',
        'tomato_fresh',
        'tomato_image',
        'tomato_meter',
        'tomato_rating',
        'tomato_reviews',
        'tomato_rotten',
        'tomato_url',
        'tomato_user_meter',
        'tomato_user_rating',
        'tomato_user_reviews'
    ]

    result = omdb.title('True Grit', tomatoes=True)
    assert set(result.keys()) == set(expected_fields)

    result = omdb.imdbid('tt0065126', tomatoes=True)
    assert set(result.keys()) == set(expected_fields)
