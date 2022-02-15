
import io
import unittest
from unittest.mock import patch
import json

from requests.models import Response, Request

import UnitTesting.MockAPI.api_process as api_process

class MockAPI():
    
    def __init__(self, url, data: dict = None):
        self.url = url
        self.data = data if data is not None else {}

    def get(self, url, params=None):

        req = Request("GET", url, params=params)
        req = req.prepare()

        response = Response()
        response.request = req
        response.url = req.url
        response.encoding = "utf-8"

        try:
            if params is None:
                response.status_code = 200
                response.raw = io.BytesIO("something that isn't latin".encode("utf-8"))
            else:
                key = params["key"]
                result = self.data.get(key)
                response.status_code = 200 if result else 404
                response.raw = io.BytesIO(json.dumps(result, ensure_ascii=False).encode("utf-8"))

        except Exception:
            response.status_code = 500
        
        return response

    def post(self, url, params=None, json=None):

        req = Request("POST", url, params=params, json=json)
        req = req.prepare()

        response = Response()
        response.request = req
        response.url = req.url
        response.encoding = "utf-8"
        response.status_code = 200

        self.data = {**self.data, **json} 

        return response

class TestAPI(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.API = MockAPI(url="https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt")
        return super().setUpClass()

    def test_api_url(self):
        with patch("api_process.requests.get") as mock_get:
            api_process.get_from_api()
            mock_get.assert_called_with(self.API.url, params=None)


    def test_get_normal(self):
        with patch("api_process.requests.get", side_effect=self.API.get):

            r = api_process.get_from_api()

            self.assertEqual(r.status_code, 200)

    def test_post_data(self):
        with patch("api_process.requests.get", side_effect=self.API.get), patch("api_process.requests.post", side_effect=self.API.post):
            key = "a"
            data = {key: 1}

            response = api_process.post_to_api(data)
            self.assertEqual(response.status_code, 200)

            response = api_process.get_from_api({"key": key})

            self.assertEqual(response.json(), data[key])
    
    @unittest.expectedFailure
    def test_fail(self):
        self.fail("Testing a fail")

if __name__ == "__main__":
    unittest.main()
