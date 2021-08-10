import requests
import json
headers = {'content-type':'application/json'}
url="http://0.0.0.0:80/api/sms/"   
data = {
    'taskId':"11",
    'shareDir':'sharedir',
    'url':'url',
    'name':'Name'
}
r = requests.post(url, data=json.dumps(data),headers=headers)
print(r.text)
