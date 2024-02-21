import unittest
from unittest.mock import patch
import app

class TestIndex(unittest.TestCase):

    @patch('app.requests.get')
    def test_index(self, mock_get):
        mock_response = {
            'rates': {'USDEUR': 1.1}
        }
        mock_get.return_value.json.return_value = mock_response

        with app.test_client() as client:
            response = client.post('/', data={
                'from_currency': 'EUR',
                'to_currency': 'USD',
                'amount': '100'
            })

            self.assertEqual(response.status_code, 200)

if __name__ == '__name__':
    unittest.main()
     