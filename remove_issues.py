import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import json
payload = {
        'username': 'divithreddyg',
        'password': 'HDPx7"^e8&%,D-q)'
}

response = requests.get(
        'https://api.github.com/repos/divithreddyg/Test/issues',
        auth=HTTPBasicAuth('divithreddyg', 'HDPx7"^e8&%,D-q)')
)

print(type(response.json()))
for responseitem in response.json():
        print("a")
        url = responseitem.get('url')
        print(type(url))
        patchbody = requests.get(url)
        x = patchbody.json()
        print(x['state'])
        x['state']='closed'
        x['closed_by']=x['user']
        d = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        x['closed_at']=d
        x['updated_at']=d
        x.pop('assignees', None)

        resp = requests.patch(url,json.dumps(x),  auth=HTTPBasicAuth('divithreddyg', 'HDPx7"^e8&%,D-q)'))


print("removed issues")
