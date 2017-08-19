import urllib
import json
phone = raw_input("Enter receiver's number: ")
msg = raw_input("Enter the message to send: ")
headers = { "X-Mashape-Authorization": "P5yR4waACAmshAdtTiVEjvFdheITp1dRuBSjs" }
url = "https://mashape.com/index.php?msg="+msg+"&phone="+phone+"&pwd='Tejaswi@9'&uid='AcharyaTejaswi'"
data=json.load(urllib.urlopen(url,'',headers))
print data
'''req = urllib2.Request(url, '', headers)
response = json.loads(urllib2.urlopen(req).read())
if response['response'] != "done\n":
    print "Error"
else:
    print "Message sent successfully"'''