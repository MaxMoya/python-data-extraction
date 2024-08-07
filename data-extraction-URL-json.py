import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url: ')
print('Retrieving:', url)
link = urllib.request.urlopen(url)

#Opening and decoding JSON
json = json.loads(link.read().decode())
print('Retrieving ', len(json['comments']), 'Users')

#Parsing and addind comments
lst = list()
for summ in json['comments']:
  lst.append(summ['count'])

print('Total comments:', sum(lst))
