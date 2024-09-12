import requests
import json
import time
import jwt
from .variables import service_account_id, key_id

def generateToken():
    with open('ml/authorized_key.json') as f:
        authorized_key = json.load(f)

    private_key = authorized_key['private_key']
    now = int(time.time())
    payload = {
            'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
            'iss': service_account_id,
            'iat': now,
            'exp': now + 360}

    encoded_token = jwt.encode(
        payload,
        private_key,
        algorithm='PS256',
        headers={'kid': key_id})
    url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
    x = requests.post(url,  headers={'Content-Type': 'application/json'}, json = {'jwt': encoded_token}).json()
    iam_token = x['iamToken']
    return iam_token  
    
