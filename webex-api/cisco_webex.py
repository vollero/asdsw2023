import requests
import json
import time

token = 'Bearer <TOKEN>'
url = 'https://api.ciscospark.com/v1/rooms'

r = requests.get(url, headers = {'Authorization': token})

if(r.status_code != 200):
    print('Errore')
    print('ERROR CODE: {}\nRESPONSE: {}'.format(r.status_code, r.text))
else:
    jsonData = r.json()
    print(json.dumps(jsonData, indent=4))

print('-'*100)

rooms = r.json()['items']
roomName = 'ADSD'
roomID = None

for room in rooms:
    print('Stanza: {} - ID: {}'.format(room['title'], room['id']))
    if(room['title'].find(roomName) != -1):
        roomID = room['id']
        break

print('room ID: {}'.format(roomID))

print('-'*100)

url = 'https://api.ciscospark.com/v1/messages'

urlParams = {
    'roomId': roomID,
    'max': 5
}

r = requests.get(url, params = urlParams, headers={'Authorization': token})

if(r.status_code != 200):
    print('Errore')
    print('ERROR CODE: {}\nRESPONSE: {}'.format(r.status_code, r.text))
else:
    jsonData = r.json()
    print(json.dumps(jsonData, indent=4))

print('-'*100)

bodyParams = {
    'roomId': roomID,
    'text': 'Questo messaggio è generato dalla mia macchina virtuale con python!'
}

r = requests.post(url, data=bodyParams, headers={'Authorization': token})

if(r.status_code != 200):
    print('Errore')
    print('ERROR CODE: {}\nRESPONSE: {}'.format(r.status_code, r.text))
else:
    jsonData = r.json()
    print(json.dumps(jsonData, indent=4))
