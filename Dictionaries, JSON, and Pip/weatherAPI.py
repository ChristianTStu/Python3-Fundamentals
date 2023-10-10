import requests

city = 'New Orleans'
url = 'http://api.weatherapi.com/v1/current.json?key=9a478a9ed39d43d1911181050231010&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print(f"Today's wethaer in {city} is {temp} degrees farhenheit and {description}.")