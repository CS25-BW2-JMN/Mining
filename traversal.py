
baseURL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/"
init = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"
key = config('')

while True:
    r = requests.get(url=baseURL + "/")