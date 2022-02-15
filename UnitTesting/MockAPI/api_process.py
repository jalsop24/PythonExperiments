
import json
import requests

GET_URL = "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"

POST_URL = "https://www.abc.com"

def get_from_api(params=None):
    
    response = requests.get(GET_URL, params=params)

    return response

def post_to_api(data):

    response = requests.post(POST_URL, json=data)

    return response

def main():
    text = get_from_api()
    print(text)

    r = post_to_api({"a": 1})
    print(r)

if __name__ == "__main__":
    main()
