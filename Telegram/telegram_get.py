import requests
import json


url = 'https://api.telegram.org/bot{0}/getUpdates'.format(token)

print(url)


response = requests.get(url)
response_json = response.json()

#print(response_json)


for i in response_json['result']:
    first_name = i['message']['chat']['first_name']
    last_name = i['message']['chat']['last_name']
    chat_id = i['message']['chat']['id']
    text = i['message']['text']
    update_id = i['update_id']
    print (first_name, last_name,chat_id,update_id,text)

print("\n \n****ESPECIFICO**** \n")

id = 382529282
for i in response_json['result']:
    pessoa_id = i['message']['from']['id']
    if id == pessoa_id:
        first_name = i['message']['chat']['first_name']
        last_name = i['message']['chat']['last_name']
        text = i['message']['text']
        print (first_name, last_name, text)




