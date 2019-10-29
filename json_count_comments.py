import urllib.request, urllib.parse, urllib.error
import ssl
import json

#ignore ssl certs
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_301559.json'
uh = urllib.request.urlopen(url, context = ctx)
data = uh.read().decode()
js = json.loads(data)
#print(data)
total = 0
for item in js['comments']:
    num = (item['count'])
    total = total + num

print(total)
