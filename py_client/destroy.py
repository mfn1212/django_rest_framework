import requests
from getpass import getpass

username = input('whats your username ?')
password = getpass('whats your password ?')
end_point = 'http://127.0.0.1:8000/api/auth/'
data = {
    "username": username,
    'password': password,
}
auth_response = requests.post(end_point, json=data)
print(auth_response.json())
if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {'authorization': f'mehran {token}'}

end_point = 'http://127.0.0.1:8000/api/product/destroy/30'
get_response = requests.delete(end_point, headers=headers)

print(get_response.json())
