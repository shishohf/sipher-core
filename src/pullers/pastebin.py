import requests
import json

class Pastebin:
    def __init__(self):
        self.limit = 1
        self.method = "api_scraping.php"
        self.pastebin_uri = "https://scrape.pastebin.com/{}?limit={}"

    def get_scrape_url(self) -> str:
        return self.pastebin_uri.format(self.method, self.limit)

    def get_limit(self) -> int:
        return self.limit

    def get_method(self) -> str:
        return self.method

    def set_limit(self, limit=1):
        self.limit = limit

    def set_method(self, method):
        self.method = method

    def scrape_records(self, limit=None) -> object:
        if limit:
            self.limit = limit
        json_string = requests.get(self.get_scrape_url())
        return json.loads(json_string.text)

    def scrape_raw_data(self, scrape_url) -> str:
        data = requests.get(scrape_url).text
        return data
