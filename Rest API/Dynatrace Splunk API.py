import requests
from requests.auth import HTTPBasicAuth
url="https://192.168.1.100:8021/api/v2/alerts"
r=requests.get(url,headers={ 'Content-Type': 'application/json'},auth=HTTPBasicAuth('admin','admin'),verify=False)
#print(r.json()['alerts'])
for id in r.json()['alerts']:
   #print(id['id'])
   #print(id['href'])
   r=requests.get(url=id['href'],headers={ 'Content-Type': 'application/json'},auth=HTTPBasicAuth('admin','admin'),verify=False)
   #print(r.json())
   if 'end' not in r.json():
       #print(r.json())
       if 'Splunk' in r.json()['rule']:
           print(r.json())