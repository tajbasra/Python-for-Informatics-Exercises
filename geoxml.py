import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

counts = tree.findall('.//comment')
counting = 0
summing = 0
    
for item in counts:
    counting += 1
    summing += int(item.find('count').text)
    
print 'Count: ', counting
print 'Sum: ', summing

