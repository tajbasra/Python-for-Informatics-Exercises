import urllib
import json

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

info = json.loads(data)
print 'Count:', len(info)

counting = 0
#print json.dumps(info, indent=4)
for item in info['comments']:
        counting += int(item['count'])


print 'Sum:', counting

