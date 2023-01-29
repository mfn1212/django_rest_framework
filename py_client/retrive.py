import requests
end_point = 'http://127.0.0.1:8000/api/product/3'
get_response = requests.get(end_point)

print(get_response.json())
