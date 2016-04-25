filename = raw_input("Enter a file name: ")
filehandle = open(filename)
filedict = dict()
lst = list()
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    lst.append(words[5])
    #print lst
    for thing in lst:
        hour = thing.find(':')
        thing = thing[:hour]
    filedict[thing] = filedict.get(thing,0)+1

anotherlst = filedict.items()
anotherlst.sort()

for key, val in anotherlst:
    print key, val
