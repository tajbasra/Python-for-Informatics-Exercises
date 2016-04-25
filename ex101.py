filename = raw_input("Enter a file name: ")
filehandle = open(filename)
filedict = dict()
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    filedict[words[1]] = filedict.get(words[1],0)+1

lst = list()
for key, val in filedict.items():
    lst.append((val,key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print val, key