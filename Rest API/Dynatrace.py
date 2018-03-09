import requests
import json
from requests.auth import HTTPBasicAuth
url="https://sgpl-drnatrace:8021/rest/management/reports/create/Dynatrace-API?type=JSON"
re=requests.get(url,auth=HTTPBasicAuth('admin','admin'),verify=False)
data = re.json()['data']
incidentsoverviewdashlet = data['incidentsoverviewdashlet']['incidentoverviewrecords']['incidentoverviewrecord']
for i,j in incidentsoverviewdashlet.iteritems():
    for k in range(len(j)):
        for m,n in j[k].iteritems():
           print n
           ''' for x in range(len(n)):
                print n[x]'''


#for i in range(len(incidentsoverviewdashlet['incidentoverviewrecords']['incidentoverviewrecord'])):
#print incidentsoverviewdashlet['incidentoverviewrecords']['incidentoverviewrecord']
#for i in incidentsoverviewdashlet['incidentoverviewrecords']['incidentoverviewrecord']:
#    print(i)