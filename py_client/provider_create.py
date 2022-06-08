import requests


# endpoint = "http://localhost:8000/api/providers/"
# data = {
#     "name": 'Adrian',
#     'phone': '+15852826576',
#     'email': 'adrian@gmail.com',
#     'language': 'german',
#     'currency': 'euro'
# }
# get_response = requests.post(endpoint, json=data)  # HTTP request
#
# print(get_response.json())

endpoint = "http://localhost:8000/api/service_areas/"
data = {
    "name": 'area 1',
    'price': 29.99,
    'polygon': {
        'type': 'Polygon',
        'coordinates': [(0.0, 0.0), (0.0, 50.0),
                        (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)]
    },
    'provider': 'golabi'
}
get_response = requests.post(endpoint, json=data)  # HTTP request

print(get_response.json())
