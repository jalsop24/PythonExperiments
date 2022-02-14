
import unittest
from unittest.mock import patch

import api_process

class MockResponse():

    def __init__(self):
        pass

class TestAPI(unittest.TestCase):
    
    def test_get(self):
        with patch("api_process.requests.get") as mock_get:
            
            response = MockResponse()
            response.text = "something that isn't latin"
            
            mock_get.return_value = response

            text = api_process.get_from_api()

            print(text)


if __name__ == "__main__":
    unittest.main()
