import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"name": 'amix', 'phone': '+18143008176', 'email': 'amix@gmail.com', 'language': 'spanish', 'currency': 'dollar'})  # HTTP request
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
