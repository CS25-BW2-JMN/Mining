from decouple import config
import requests
init = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"
key = config('API')
map = open('map.txt', 'w')
rooms = open('rooms.txt', 'w')
headers = {'Authorization': 'Token ' + key}
r = requests.get(init, headers=headers)
data = r.json()
traversal = {data['room_id']: {}}
room = {data['room_id']: [data['coordinates'], data['title']]}
for exit in data['exits']:
    traversal[data['room_id']][exit] = '?'
map.write(str(traversal))
rooms.write(str(room))
