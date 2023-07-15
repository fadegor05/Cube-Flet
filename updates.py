from config import *
import requests
import json

def update_loop(is_first):
    print(get_server_latest())

def get_server_latest():
    req = json.loads(requests.get(SERVER_ADDRESS).text)
    return {'version': req[1], 'title': req[2], 'date': req[3], 'text': req[4]}