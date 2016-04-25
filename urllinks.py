# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

def anchortags(url):
    soup = BeautifulSoup(urllib.urlopen(url).read())
# Retrieve all of the anchor tags
    tags = soup('a')
    return tags

tags = anchortags(raw_input('Enter - '))

position = int(raw_input('Enter position:'))
count = int(raw_input('Enter count:'))
counting = 0

while counting < (count - 1):
    url = tags[position-1].get('href', None)
    print 'Retrieving:', url
    tags = anchortags(url)
    counting += 1


url = tags[position-1].get('href', None)
print 'Last URL', url



