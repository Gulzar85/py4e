import urllib.request, urllib.parse, urllib.error
import json

lst = list()

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
for item in js['comments']:
    lst.append(item['count'])
print('count: ', len(lst))
print('sum: ', sum(lst))










