from decouple import config
from datetime import datetime, timedelta
import requests
from ast import literal_eval
baseURL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/"
key = config('4f18243e2c6cbc6c63dcdf152cfcb7cd854a3fa9')
headers = {'Authorization': 'Token ' + key}

# INIT
r = requests.get(baseURL + 'init', headers=headers)
data = r.json()

# READ FILES FOR HISTORY OF MAP
traversal_graph = literal_eval(open('map.txt', 'r').read())
rooms = literal_eval(open('rooms.txt','r').read())

# OPPOSITE DIRECTIONS
opposite = {'n': 's', 'w':'e', 's': 'n', 'e':'w'}

while True:
    room = data['room_id']
    if room not in traversal_graph:
        traversal_graph[room] = {}
        for exit in data['exits']:
            traversal_graph[room][exit] = '?'
    print(data['coordinates'] + 'You are in room ' + str(data['room_id']) + '. ' + data['title'] + ': ' + data['description'])
    print("MESSAGES FROM THE SERVER")
    for message in data['messages']:
        print(message)w
    print("ITEMS")
    for item in data['items']:
        print(item)
    print(" ")
    print('Possible directions are: ' + str(data['exits']))
    print('YOUR COOLDOWN IS: ' + str(data['cooldown']))
    print(" ")
    print('Waiting for cooldown to finish...')
    avail_time = datetime.now() + timedelta(seconds=data['cooldown'])
    while datetime.now() < avail_time:
        pass
    ans = input('What direction do you want to go in? Press q to quit! ')
    if not ans:
        break
    ans = ans[0]
    print(" ")
    if ans == 'q':
        break
    elif ans in data['exits']:
        prev_data = data
        # if traversal_graph.get(data['room_id'], None) and traversal_graph.get(data['room._id'], None)
        if traversal_graph.get(data['room_id']):
            if traversal_graph[data['room_id']][ans] != '?':
                next_room = traversal_graph[data['room_id']][ans]
                r = requests.post(url=baseURL + 'fly', json={'direction': ans, 'next_room_id': str(next_room)}, headers=headers)
            else:
                r = requests.post(url=baseURL + 'fly', json={'direction': ans}, headers=headers)
        else:
            r = requests.post(url=baseURL + 'fly', json={'direction': ans}, headers=headers)
        data = r.json()
        room = data['room_id']
        rooms[room] = [data['coordinates'], data['title'], data['description']]
        if room not in traversal_graph:
            traversal_graph[room] = {}
            for exit in data['exits']:
                traversal_graph[room][exit] = '?'
        traversal_graph[room][opposite[ans]] = prev_data['room_id']
        traversal_graph[prev_data['room_id']][ans] = room

# Write graph to file
new_map = open('map.txt','w')
print("{", file=new_map)
for room in traversal_graph:
    print(f"  {room}: {traversal_graph[room]},", file=new_map)
print("}", file=new_map)
new_map.close()

# Write rooms to file
new_rooms = open('rooms.txt','w')
print("{", file=new_rooms)
for room in rooms:
    print(f"  {room}: {rooms[room]},", file=new_rooms)
print("}", file=new_rooms)
new_rooms.close()