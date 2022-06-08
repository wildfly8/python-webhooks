import requests
import json

webhook_url = 'https://webhook.site/03107233-0f88-4d68-b2c9-91b644b9fbfb'

data = { 'name': 'DevOps Journey', 
         'Channel URL': 'test url5' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})