from decouple import config
import hashlib
from datetime import datetime, timedelta
import requests
import random
from ast import literal_eval
baseURL = "https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof"
key = config('API')
headers = {'Authorization': 'Token ' + key}

# r = requests.get(url=baseURL, headers=headers)
# data = r.json()
# last_proof = data['proof']
# diff = data['difficulty']
def proof(last_proof, diff):
    proof = 10000000
    while valid_proof(last_proof, proof, diff) is not True:
        # proof = random.randint(9000000,15293900900)
        # print(proof)
        if proof > 1500000000:
            proof = 1234567
        val = random.randint(1,1111)
        val *= random.randint(1,3)
        proof += val
    return proof
def valid_proof(last_proof, proof, diff):
    return hashlib.sha256(f'{last_proof}{proof}'.encode()).hexdigest()[:diff] == '0'*diff
while True:
    r = requests.get(url=baseURL, headers=headers)
    data = r.json()
    last_proof = data['proof']
    diff = data['difficulty']
    ans = proof(last_proof, diff)
    r = requests.post(url="https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/", json={"proof":ans}, headers=headers)
    data = r.json()
    avail_time = datetime.now() + timedelta(seconds=data['cooldown'])
    print('Cooldown of ' + str(data['cooldown']) + '...')
    while datetime.now() < avail_time:
        pass
    print(data)