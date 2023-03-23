import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    location = input('Enter location: ')
    if len(location) < 1 : break

    parms = dict()
    parms['address'] = location
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieving',len(data),'characters')

    js = json.loads(data)

    #print(json.dumps(js, indent=4))

    place_id = js['results'][0]['place_id']
    print('place_id:',place_id)
    
    break