import json
#import urllib
import requests
import unirest
#url = "http://api.openweathermap.org/data/2.5/weather?q=Beeramguda,IN&APPID=edb1f5255d318a18c5e9b61debb6a5a9"
#url2="http://api.datayuge.in/v3/rechargeplans/?apikey=P5yR4waACAmshAdtTiVEjvFdheITp1dRuBSjs&operatorid=uninor&circleid=andhra pradesh"
#url3="http://api.datayuge.in/v1/mnp?apikey=P5yR4waACAmshAdtTiVEjvFdheITp1dRuBSjs&number=7794029809"
#url4="https://AcharyaTejaswi:tejaswi9@datayuge-whatsapp-api-unofficial.p.mashape.com/v1/whatspusher?apikey=P5yR4waACAmshAdtTiVEjvFdheITp1dRuBSjs&no=917794029809&txtmsg=Hello+Bro"
#response = requests.get(url3)
response = unirest.post("https://datayuge-whatsapp-api-unofficial.p.mashape.com/v1/whatspusher?audmsg=&no=917794029809&picmsg=&txtmsg=Hello+Bro&vidmsg=&apikey=",headers={"X-Mashape-Key": "RJ0MSDmo67mshILRp2aP7RT0AHf7p19vK6WjsnVzVahaRqXlQA","Accept": "application/json"}).raw_body
print response
