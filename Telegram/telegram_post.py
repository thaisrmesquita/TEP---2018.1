import requests
import json


url = 'https://api.telegram.org/bot{0}/sendMessage'.format(token)

data = {'chat_id': 484389444, 'text': 'Teste Post'}

response = requests.post(url, data = data)

print(response.content)