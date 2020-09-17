import requests
import os
import random
import json
import string


random.seed = (os.urandom(1024))

url = "http://127.0.0.1:5000/"

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra
    requests.post(url, allow_redirects=False, data={
        "player": username 
    })

print(f"Sending username: {username}")

