filename = raw_input("Enter a file name: ")
filehandle = open(filename)
filedict = dict()
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    filedict[words[1]] = filedict.get(words[1],0)+1

bigcount = None
bigword = None
for word,count in filedict.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount