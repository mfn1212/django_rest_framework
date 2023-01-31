import requests

end_point = 'http://127.0.0.1:8000/api/product/mixin_view/'
#           list
get_response = requests.get(end_point)
print(get_response.json())
#           retrive
get_response = requests.get(end_point + "2/")
print(get_response.json())
#           create
data = {
    'title': "a32",
    # 'content': "a32 is not fast",
    'price': 133,
}
get_response = requests.post(end_point, json=data)
print(get_response.json())

#           update
data = {
    'title': "a32",
    'content': None,
    # 'content': '122',
    'price': 133,
}
get_response = requests.post(end_point+"2/", json=data)
print(get_response.json())
