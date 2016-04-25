import urllib


#addressurl = raw_input('Enter the URL of a txt file:')

try:
    fhand = urllib.urlopen(raw_input('Enter the URL of a txt file:'))
    
    length = 0

    for data in fhand:
        line = data.strip()
        length += len(line)
        if length <= 3000:
            print line;
    print 'Total number of characters are:', length
except:
    print 'Webage cannot be opened'