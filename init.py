from decouple import config
init = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"
map = open('map.txt', 'w')
rooms = open('rooms.txt', 'w')
key = config('API')