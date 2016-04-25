filename = raw_input("Enter a file name: ")
filehandle = open(filename)
filedict = dict()
lst = list()
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    lst.append(words[1])
    for thing in lst:
        domain = thing.find('@')
        thing = thing[domain+1:]
    filedict[thing] = filedict.get(thing,0)+1

    

print filedict