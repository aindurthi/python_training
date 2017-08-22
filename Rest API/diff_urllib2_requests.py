import urllib2
import urllib
import json

# Specify the url
url = 'http://www.pythonforbeginners.com'

# This packages the request (it doesn't make it)
request = urllib2.Request(url)

# Sends the request and catches the response
response = urllib2.urlopen(request)

# Extracts the response
print response.read()
