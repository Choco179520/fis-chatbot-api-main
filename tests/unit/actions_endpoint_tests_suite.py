import unittest
import requests


class ActionsEndpointTestSuite(unittest.TestCase):

    def test_actions_endpoint_status(self):
        url = 'http://127.0.0.1:5000/api/actions'

        data = {'action': 'tipos-matriculas'}
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
