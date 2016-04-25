fword = raw_input("Enter file name: ")
fhand = open(fword)
counting = fhand.read()
counting = counting.split()
words = dict()
for item in counting:
    words[item] = 1

print words