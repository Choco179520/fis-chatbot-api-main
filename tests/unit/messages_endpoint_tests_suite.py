import unittest
import requests


class MessagesEndpointTestSuite(unittest.TestCase):

    def test_messages_endpoint_status(self):
        url = 'http://127.0.0.1:5000/api/messages'

        data = {'user_message': 'Hola'}
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
