
from unittest import TestCase

import pytest
from requests.exceptions import Timeout

import omdb


class TestClient(TestCase):

    def setUp(self):
        self.client = omdb.Client()

    def test_request(self):
        req = {'t': 'True Grit', 'y': '1969'}
        res = self.client.request(**req)

        self.assertTrue(res.ok)

        data = res.json()

        self.assertEqual(data['Title'], req['t'])
        self.assertEqual(data['Year'], req['y'])

    def test_get(self):
        req = {'title': 'True Grit',
               'year': '1969',
               'fullplot': True,
               'tomatoes': True}
        data = self.client.get(**req)

        self.assertEqual(data['title'], req['title'])
        self.assertEqual(data['year'], req['year'])
        self.assertTrue('tomato_meter' in data)

    def test_set_default(self):
        req = {'title': 'True Grit'}

        data = self.client.get(**req)

        # default request returns movie with this year
        self.assertEqual(data['year'], '2010')

        # change the default year and re-request
        self.client.set_default('year', '1969')

        data = self.client.get(**req)

        # default year is now used
        self.assertEqual(data['year'], '1969')

        # can also set defaults at client instantiation time
        self.client = omdb.Client(year='1969')

        data = self.client.get(**req)

        self.assertEqual(data['year'], '1969')

        # defaults can be overridden
        req = {'title': 'True Grit', 'year': '2010'}
        data = self.client.get(**req)

        self.assertEqual(data['year'], '2010')

    def test_timeout(self):
        with pytest.raises(Timeout):
            self.client.get(title='True Grit', timeout=0.0001)

        self.client.set_default('timeout', 0.0001)

        with pytest.raises(Timeout):
            self.client.get(title='True Grit')
