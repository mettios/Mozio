import requests

endpoint = "http://localhost:8000/api/providers/3/update/"

data = {
    'language': 'Farsi',
    'email': 'aydin@yahoo.com',
    'phone': '+34631164732',
    'currency': 'Rial',
    'name': 'Aydin'
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
