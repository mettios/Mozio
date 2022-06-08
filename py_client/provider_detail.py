import requests

endpoint = "http://localhost:8000/api/providers/1/"

get_response = requests.get(endpoint, json={"name": 'aydin', 'phone': '+34631164732', 'email': 'aydin@gmail.com', 'language': 'persian', 'currency': 'rial'})  # HTTP request

print(get_response.json())
