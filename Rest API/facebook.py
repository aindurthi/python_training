import requests
import urllib2
import json
#TARGET_ID = '145634995501895'
TARGET_ID='1456575324641474'
#ACCESS_TOKEN = 'f51dfe6f51792d71b186f499f8720f63'
ACCESS_TOKEN='1456575324641474|xmX-9jtoqHOfqFCWRXMIdRxqBJk'
#payload = {"fields": "statuses" "access_token": ACCESS_TOKEN}
token = {"access_token": ACCESS_TOKEN}
api_endpoint ="https://graph.facebook.com/"
#test_api="https://www.facebook.com?id=me"
#test_api="https://www.facebook.com/profile.php?id=me&fref=ts"
test_api="https://graph.facebook.com/me/friends"
req=requests.get(test_api+TARGET_ID+"&access_token="+ACCESS_TOKEN)
#req = requests.get(api_endpoint+TARGET_ID+"?fields=id,name&access_token="+ACCESS_TOKEN)
#req = requests.get(api_endpoint+TARGET_ID)
print req.content
#response=requests.get('https://www.facebook.com/profile.php?id=1456575324641474&fref=ts')
#response = requests.get("https://graph.facebook.com/app?id=1456575324641474")
#print response



'''import requests
#r = requests.get('https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=1456575324641474&client_secret=f51dfe6f51792d71b186f499f8720f63')
#access_token = r.text.split('=')[1]
response=requests.get('https://developers.facebook.com/apps/1456575324641474/')
print response'''