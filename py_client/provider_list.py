import requests

endpoint = "http://localhost:8000/api/providers/"

get_response = requests.get(endpoint)  # HTTP request

print(get_response.json())
