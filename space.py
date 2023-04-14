from pprint import pprint
import requests

link = 'http://api.open-notify.org/astros.json'

response = requests.get(link)
response_json = response.json()
pprint(response_json)

print("The current people in space are: ")
for person in response_json['people']:
    print(person['name'])