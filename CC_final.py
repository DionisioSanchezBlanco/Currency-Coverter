from requests import get
from json import loads

class Coin:
    cache = {}

    def __init__(self, currency, exchange, quantity):
        self.currency = currency
        self.exchange = exchange
        self.quantity = quantity

    def coin_to_coin(self, rate):
        print(f"You received {self.quantity * rate} {self.exchange.upper()}.")

    def rate_coin(self):
        if self.exchange in coin.cache:
            print("Oh! It is in the cache!")
            return float(coin.cache[self.exchange])
        else:
            print("Sorry, but it is not in the cache!")
            coin.cache[self.exchange] = dict_coins[self.exchange]["rate"]
            return float(dict_coins[self.exchange]["rate"])

    def default_cache(self, dict_coins):
        if coin.currency == "eur":
            coin.cache['usd'] = dict_coins['usd']["rate"]
        elif coin.currency == "usd":
            coin.cache['eur'] = dict_coins['eur']['rate']
        else:
            coin.cache['usd'] = dict_coins['usd']["rate"]
            coin.cache['eur'] = dict_coins['eur']['rate']

coin = Coin(input(), input(), int(input()))

# Get the json file only once for the coin to change
url = "http://www.floatrates.com/daily/" + coin.currency + ".json"

# Get the JSON content from website
r = get(url).content

# Load the json STRING (loads) to create the dictionary
dict_coins = loads(r)

coin.default_cache(dict_coins)

while coin.exchange:
    print("Checking the cache…")
    rate = coin.rate_coin()
    coin.coin_to_coin(rate)

    coin.exchange = input()
    if coin.exchange == "":
        break
    coin.quantity = int(input())