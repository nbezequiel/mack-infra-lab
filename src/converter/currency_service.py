import requests
import json


class CurrencyService:

    def __init__(self):
        self._currencies_bases = {'USD': 'dolar', 'EUR': 'euro'}
        self._BASE_URL = "https://economia.awesomeapi.com.br"

    def fetch(self, base: str) -> int:
        URL = "%s/json/last/%s" % (self._BASE_URL, base)
        response = requests.get(URL)
        return json.loads(response.content)['%sBRL' % base]['ask']
