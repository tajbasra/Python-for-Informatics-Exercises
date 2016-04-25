filename = raw_input("Enter a file name: ")
filehandle = open(filename)
filedict = dict()
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    filedict[words[2]] = filedict.get(words[2],0)+1
print filedict