filename = raw_input("Enter a file name: ")
filehandle = open(filename)
import string
filedict = dict()
lst = []
for line in filehandle:
    line = line.translate(None, string.punctuation)
    line = line.translate(None, string.digits)
    line = line.lower()
    line = line.split()
    for t in line:
        word = list(t)
        for letter in word:
            filedict[letter]=filedict.get(letter,0)+1
letterlist = []
for letter, count in filedict.items():
    letterlist.append((count,letter))
letterlist.sort(reverse=True)
for count, letter in letterlist:
    print letter, count

   