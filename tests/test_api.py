
from unittest import TestCase

import omdb


class TestApi(TestCase):

    def test_search(self):
        s = 'True Grit'
        data = omdb.search(s)

        self.assertEqual(data[0].title, s)

    def test_imdbid(self):
        i = 'tt0065126'
        data = omdb.imdbid(i)

        self.assertEqual(data.imdb_id, i)

    def test_title(self):
        t = 'True Grit'
        data = omdb.title(t)

        self.assertEqual(data.title, t)

    def test_set_default(self):
        t = 'True Grit'

        self.assertEqual(omdb.title(t).year, '2010')

        omdb.set_default('year', '1969')

        self.assertEqual(omdb.title(t).year, '1969')

    def test_get(self):
        self.assertEqual(omdb.get(title='True Grit').title, 'True Grit')
        self.assertEqual(omdb.get(imdbid='tt0065126').imdb_id, 'tt0065126')
        self.assertEqual(omdb.get(search='True Grit')[0].title, 'True Grit')

    def test_empty_data(self):
        invalid = 'asdfghjkl'

        self.assertEqual(omdb.search(invalid), [])
        self.assertEqual(omdb.title(invalid), {})
        self.assertEqual(omdb.imdbid(invalid), {})

    def test_search_model_fields(self):
        expected_fields = [
            'title',
            'year',
            'type',
            'imdb_id'
        ]

        for item in omdb.search('True Grit'):
            self.assertEqual(set(item.keys()), set(expected_fields))

    def test_get_model_fields(self):
        expected_fields = [
            'actors',
            'director',
            'genre',
            'plot',
            'poster',
            'rated',
            'released',
            'runtime',
            'title',
            'type',
            'writer',
            'year',
            'imdb_id',
            'imdb_rating',
            'imdb_votes'
        ]

        self.assertEqual(set(omdb.title('True Grit').keys()), set(expected_fields))
        self.assertEqual(set(omdb.imdbid('tt0065126').keys()), set(expected_fields))

    def test_get_model_fields_tomatoes(self):
        expected_fields = [
            'actors',
            'director',
            'genre',
            'plot',
            'poster',
            'rated',
            'released',
            'runtime',
            'title',
            'type',
            'writer',
            'year',
            'imdb_id',
            'imdb_rating',
            'imdb_votes',

            'box_office',
            'dvd',
            'production',
            'website',
            'tomato_consensus',
            'tomato_fresh',
            'tomato_image',
            'tomato_meter',
            'tomato_rating',
            'tomato_reviews',
            'tomato_rotten',
            'tomato_user_meter',
            'tomato_user_rating',
            'tomato_user_reviews'
        ]

        self.assertEqual(set(omdb.title('True Grit', tomatoes=True).keys()), set(expected_fields))
        self.assertEqual(set(omdb.imdbid('tt0065126', tomatoes=True).keys()), set(expected_fields))
