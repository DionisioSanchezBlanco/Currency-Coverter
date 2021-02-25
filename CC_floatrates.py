import requests
import json

url = "http://www.floatrates.com/daily/" + input().lower() + ".json"

# Get the content of de JSON from website
r = requests.get(url).content

# Load the json STRING (loads) to create the dictionary
dict_coins = json.loads(r)

print(dict_coins["usd"])
print(dict_coins["eur"])