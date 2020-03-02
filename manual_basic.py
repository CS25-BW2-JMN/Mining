from decouple import config
from datetime import datetime, timedelta
import requests
baseURL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/"
key = '4f18243e2c6cbc6c63dcdf152cfcb7cd854a3fa9'
headers = {'Authorization': 'Token ' + key}
r = requests.get(baseURL + 'init', headers=headers)
data = r.json()

def prompt_user():
    ans = input('What direction do you want to go in? Press q to quit! ')
    ans = ans[0]
    return ans
while True:
    print('You are in room ' + str(data['room_id']))
    print(data['coordinates'])
    print(data['title'] + ':' + data['description'])
    print('Possible directions are: ' + str(data['exits']))
    print('YOUR COOLDOWN IS: ' + str(data['cooldown']))
    print('Waiting for cooldown to finish...')
    print('YOUR COORDINATES ARE ' + (data['coordinates']))
    avail_time = datetime.now() + timedelta(seconds=data['cooldown'])
    while datetime.now() < avail_time:
        pass
    ans = input('What direction do you want to go in? Press q to quit! ')
    ans = ans[0]
    if ans == 'q':
        break
    else:
        r = requests.post(url=baseURL + 'move', json={'direction': ans}, headers=headers)
        data = r.json()
