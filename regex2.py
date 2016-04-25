import re
newlist = open(raw_input("enter a filename:")).read().split()
anotherlist = []
for thing in newlist:
     for number in re.findall('[0-9]+', thing):
        anotherlist.append(int(number))
print sum(anotherlist)