
import json
import requests

GET_URL = "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"

POST_URL = ""

def get_from_api():
    
    response = requests.get(GET_URL)

    return response.text

def post_to_api(data):

    response = requests.post(POST_URL, json=data)


def main():
    text = get_from_api()
    print(text)

if __name__ == "__main__":
    main()
