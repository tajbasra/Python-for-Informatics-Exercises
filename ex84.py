fname = raw_input('Enter the file name: ')
fhand = open(fname)
newlist = ''
for line in fhand:
    #line = line.rstrip()
    newlist = newlist + line
    shakes = newlist.split()

newshakes = list()

for i in shakes:
    if i in newshakes: continue
    else:
        newshakes.append(i)

newshakes.sort()
print newshakes
    