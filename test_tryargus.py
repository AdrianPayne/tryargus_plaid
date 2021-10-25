import unittest

from tryargus import app

# Unit Test


# Integration Test
class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.payload = {'public_token': 'public_token'}

    # /
    def test_health(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Healthy")

    # /exchange
    def test_exchange(self):
        response = self.client.post('/exchange', json=self.payload)
        self.assertEqual(response.status_code, 201)

    # /query
    def test_query_without_exchange_before(self):
        response = self.client.post('/query', json=self.payload)
        self.assertEqual(response.status_code, 404)

    def test_query_ok(self):
        response = self.client.post('/exchange', json=self.payload)
        response = self.client.post('/query', json=self.payload)

        self.assertEqual(response.status_code, 201)

    # /account
    def test_account(self):
        expected_resp = {'foo': 'bar'}

        response = self.client.get('/account', json=self.payload)

        self.assertDictEqual(response.get_json(), expected_resp)
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()

