import re
newfile = raw_input('Enter a file:')
hand = open(newfile)
newlist = []
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        print x
        for thing in x:
            thing = int(thing)
            newlist.append(thing)
print sum(newlist)