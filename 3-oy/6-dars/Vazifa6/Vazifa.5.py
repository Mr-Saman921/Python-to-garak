import requests

class DummyJson:
    def __init__(self, url):
        self.url = url

    def request(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            print(data)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

url = "https://dummyjson.com/users"
dummy_json = DummyJson(url)
dummy_json.request()
