import requests
import urllib.parse

#variables
geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Sao Paulo, Brasil"
loc2 = "Baltimore, Maryland"
key = "8b648984-498a-45ee-8765-33aae4e05ab1"
url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code
print(json_data)

