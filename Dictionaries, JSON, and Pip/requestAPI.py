import requests

#Submits the HTTP request to URL to reterive response
response = requests.get('http://api.open-notify.org/astros.json')
#Converts the response into a JSON file
json = response.json()

print('The people currently in space are:')
#Narrows down JSON file to just the "People's Dictionary" from teh JSON File
for person in json['people']:
#Narrows down further to list out just the name of those indivuals and no other data
    print(person['name'])