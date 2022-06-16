import requests

res = requests.get('https://dog.ceo/api/breed/hound/images')

dogs = res.json().get('message')

print(type(dogs))
