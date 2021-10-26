import unittest
import pytest
from application import application
from plaid_client import get_public_token

# Unit Test


# Integration Test
class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = application
        self.client = self.app.test_client()
        self.public_token = {'public_token': get_public_token()}

    # /
    def test_health(self):
        response = self.client.get('/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(b"Healthy", response.data)

    # /exchange
    def test_exchange(self):
        response = self.client.post('/exchange', json=self.public_token)

        from application import access_token

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(access_token)

    # /query
    @pytest.mark.first
    def test_query_without_exchange_before(self):
        response = self.client.post('/query')

        self.assertEqual(404, response.status_code)

    def test_query_ok(self):
        self.client.post('/exchange', json=self.public_token)
        response = self.client.post('/query')

        from application import investment_and_transaction_data

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(investment_and_transaction_data)

    # /account
    def test_account_ok(self):
        self.client.post('/exchange', json=self.public_token)
        self.client.post('/query')
        response = self.client.get('/account')

        from application import investment_and_transaction_data

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(investment_and_transaction_data)


if __name__ == "__main__":
    unittest.main()
