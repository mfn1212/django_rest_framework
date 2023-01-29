import requests
end_point = 'http://127.0.0.1:8000/api/home'
get_response = requests.get(end_point)
print(get_response.json())
