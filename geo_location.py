import urllib.request, urllib.parse, urllib.error
import ssl
import json

#ignore cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
while True:
    address = input('Type desired location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Recieving specific url...', url)

    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('**Failure to download json**')
        print(data)
        continue

    #print(json.dumps(js, indent = 4))
    print(js['results'][0]['place_id'])
