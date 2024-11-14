import unittest
import requests
from api import APIHelper
from unittest import mock


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mock_requests_post(*args, **kwargs):
    if args[0] == 'http://crossmint-challenge.io/34536456':
        return MockResponse({"goal": [["SPACE", "SPACE"], ["POLYANET", "SPACE"]]}, 200)
    return MockResponse(None, 500)


class TestAPIHelper(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch('requests.post', side_effect=mock_requests_post)
    def test_post_request_success(self, mock_post):
        url = 'http://crossmint-challenge.io/34536456'
        response = APIHelper.generate_post_request(url, {})
        self.assertNotEqual(response.json(), None)
        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.post', side_effect=mock_requests_post)
    def test_post_request_error(self, mock_post):
        url = 'https://challenge.crossmint.io/api/5685125'
        response = APIHelper.generate_post_request(url, {})
        self.assertEqual(response.json(), None)
        self.assertEqual(response.status_code, 500)


if __name__ == "__main__":
    unittest.main()