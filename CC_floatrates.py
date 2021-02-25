from requests import get
from json import loads

url = "http://www.floatrates.com/daily/" + input().lower() + ".json"

# Get the JSON content from website
r = get(url).content

# Load the json STRING (loads) to create the dictionary
dict_coins = loads(r)

print(dict_coins["usd"])
print(dict_coins["eur"])