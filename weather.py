import requests
from pprint import pprint

# api_key = 'd73af82268fa4a64a3c200007231402'
city_name = 'Buenos Aires'
link = 'http://api.weatherapi.com/v1/current.json?key=d73af82268fa4a64a3c200007231402&q='+city_name+'&aqi=no'

response = requests.get(link)
response_json = response.json()
# pprint(response_json)
# city = response_json['location']['name']
# temp = response_json['current']['temp_c']
# condition = response_json['current']['condition']['text']

city = response_json.get('location').get('name')
temp = response_json.get('current').get('temp_c')
condition = response_json.get('current').get('condition').get('text')

print(f'The weather in {city} today is {temp} degrees and {condition}')
