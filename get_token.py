from urllib.parse import urlencode
import requests

APP_ID = 6413185
AUTH_URL = 'https://oauth.vk.com/authorize'
params = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.73'
}

response = requests.get('?'.join([AUTH_URL, urlencode(params)]))

print('?'.join([AUTH_URL, urlencode(params)]))