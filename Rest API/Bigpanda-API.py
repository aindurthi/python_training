'''import requests
from requests.auth import HTTPBasicAuth
import json

headers = {
   "Authorization": "Bearer 7c562d8f450b8036c8234a93f9f243bf"
}

#data={"check": "CPU","level": "1","name": "Monitoring"}
#URL="https://api.bigpanda.io/resources/v1.0/enrichments/5a8d53180755c39404d8a82b/map"
URL="https://api.bigpanda.io/data/v2/alerts"
#data = { "app_key" : "a56dd535c4aa2f895bdda9bd2eb0a1c7", "status" : "critical", "host" : "localhost", "check" : "Testing using python script"}
data = {
  "app_key": "a56dd535c4aa2f895bdda9bd2eb0a1c7",
  "status": "warning",
  "host": "production-database-1",
  "timestamp": 1402303570, # 09 Jun 2014 08:46:10 GMT
  "application": "Billing",
  "description": "CPU is above warning limit (40%)",
  "primary_property": "application",
  "secondary_property": "host"
}
#r=requests.post(URL,headers=headers,data=json.dumps(data))
r=requests.post(URL,headers=headers,params=data)
print (r.text)'''

import requests
import bigpanda
bigpanda_client = bigpanda.Client(api_token="7c562d8f450b8036c8234a93f9f243bf", app_key="a56dd535c4aa2f895bdda9bd2eb0a1c7")
alert = bigpanda_client.alert("warn", "host1", "ping check")
alert.send()
headers={"Authorization": "Bearer 7c562d8f450b8036c8234a93f9f243bf"}
URL="https://api.bigpanda.io/resources/v1.0/incidents/5a4f5dff287189bd377f5e03/alerts/"
re=requests.get(URL,headers=headers)
print re.json()


'''import bigpanda
import socket
import ssl
import logging
import json
import struct
#logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(asctime)s - %(message)s", filename='C:\\Users\\admin\\Google Drive\\acharya\\Bigpanda\\bigpanda.log')

bp=bigpanda.Client(api_token='7c562d8f450b8036c8234a93f9f243bf', app_key='a56dd535c4aa2f895bdda9bd2eb0a1c7')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('api.bigpanda.io', 443))
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
#s.sendall("GET / HTTP/1.1\r\nHost: bigpanda.io\r\nConnection: close\r\n\r\n")
s.sendall("POST /data/v2/alerts HTTP/1.1")
data = s.recv()
print (data)
while 1:
      alert = bp.alert("warn","tetc","Ping")
      alert.send()'''

