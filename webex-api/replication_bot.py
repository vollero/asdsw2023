import requests
import json
import time
import datetime

token = 'Bearer <TOKEN>'

url = 'https://api.ciscospark.com/v1/rooms'

r = requests.get(url, headers = {'Authorization': token})

if(r.status_code != 200):
    print('Errore')
    print('ERROR CODE: {}\nRESPONSE: {}'.format(r.status_code, r.text))
else:
    jsonData = r.json()
    #print(json.dumps(jsonData, indent=4))

#print('-'*100)

rooms = r.json()['items']

roomName = 'ADSD'
roomID_source= None
for room in rooms:
    print('Stanza: {} - ID: {}'.format(room['title'], room['id']))
    if(room['title'].find(roomName) == 0):
        roomID_source = room['id']
        break

roomName = 'Replicazione'
roomID_destination= None
for room in rooms:
    print('Stanza: {} - ID: {}'.format(room['title'], room['id']))
    if(room['title'].find(roomName) == 0):
        roomID_destination = room['id']
        break

print('Starting replication from \nroom ID: {} \nto \nroom ID: {}'.format(roomID_source, roomID_destination))

print('-'*100)

url = 'https://api.ciscospark.com/v1/messages'

urlParams_source = {
    'roomId': roomID_source,
    'max': 1
}

id_mes_old = 0

while True:
    time.sleep(0.5)
    r = requests.get(url, params = urlParams_source, headers={'Authorization': token})

    testo   = r.json()['items'][0]['text']
    id_mes  = r.json()['items'][0]['id']
    id_per  = r.json()['items'][0]['personId']

    urlPeople = 'https://api.ciscospark.com/v1/people/' + id_per

    if not id_mes == id_mes_old:

        r2 = requests.get(urlPeople, headers={'Authorization': token})
        name = r2.json()['displayName']
        
        if(not name.find('Luca Vollero') == -1):

            bodyParams = {
                'roomId': roomID_destination,
                'text': name + ': ' + testo
                }
            time.sleep(0.5)
            r = requests.post(url, data=bodyParams, headers={'Authorization': token})
            id_mes_old = id_mes
