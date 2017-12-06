#!/usr/bin/env python
import requests

tc_url = "http://10.6.98.57:9999"
auth = "__TCUser__", "__TCPass__"

headers = {'Accept': 'application/json'}

id_arr = []
url = tc_url + "/app/rest/agents?includeUnauthorized=true"
req = requests.get(url, headers=headers, auth=auth, timeout=10).json()

for i in range(0, len(req['agent'])):
    id = req['agent'][i]['id']
    url = tc_url + "/app/rest/agents/id:{}/authorized".format(id)
    data = "true"
    req_put = requests.put(url, auth=auth, data=data, timeout=10)