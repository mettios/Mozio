import requests

provider_id = 7
endpoint = f"http://localhost:8000/api/providers/{provider_id}/delete/"
get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code == 204)
