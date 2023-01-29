import requests
end_point = 'http://127.0.0.1:8000/api/product/destroy/4'
get_response = requests.delete(end_point)

print(get_response.json())
