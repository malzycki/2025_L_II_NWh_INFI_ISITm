import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        # Dekodujemy odpowiedź z serwera do słownika
        data = json.loads(rv.data)

        # Sprawdzamy konkretne klucze i wartości
        self.assertEqual(data['imie'], "Michał")
        self.assertEqual(data['msg'], "Hello World!")
