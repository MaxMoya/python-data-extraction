import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open url and parse xml
url = input('Enter url: ')
print('Retrieving', url)
link = urllib.request.urlopen(url, context=ctx)
data = link.read()
print('Retrieving', len(data), 'characters')
tree = ET.fromstring(data)
comms = tree.findall('comments/comment')
comcount = len(comms)
com_total = 0

for comm in comms:
    com_total += float(comm.find('count').text)

print(comcount)
print(com_total)