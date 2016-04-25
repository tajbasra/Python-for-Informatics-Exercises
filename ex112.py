import re
newfile = raw_input('Enter a file:')
hand = open(newfile)
newlist = []
for line in hand:
    line = line.rstrip()
    x = re.findall('^.*New Revision: ([0-9]+).*', line)
    if len(x) > 0:
        for thing in x:
            thing = float(thing)
            newlist.append(thing)

    
average = sum(newlist)/len(newlist)
print average