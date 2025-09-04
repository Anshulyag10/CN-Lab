import requests
import logging

logging.basicConfig(filename="http_client.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def do_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "userId": 7,
        "title": "Posting via Python",
        "body": "Sample text created for testing purpose."
    }
    try:
        r = requests.post(url, json=data)
        print("POST Request")
        print("Code:", r.status_code)
        print("Headers:", dict(r.headers))
        print("Response:", r.json())
    except Exception as e:
        logging.exception("POST request failed")
        print("POST failed:", e)

def do_get():
    url = "https://jsonplaceholder.typicode.com/posts/2"
    try:
        r = requests.get(url)
        print("\nGET Request")
        print("Code:", r.status_code)
        print("Headers:", dict(r.headers))
        print("Response:", r.json())
    except Exception as e:
        logging.exception("GET request failed")
        print("GET failed:", e)

do_post()
do_get()
