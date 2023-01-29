import requests
end_point = 'http://127.0.0.1:8000/api/product/update/5/'
data = {
    'title': "a32",
    'content': "a32 is fast",
    'price': 133,
}
get_response = requests.patch(end_point, json=data)

print(get_response.json())
