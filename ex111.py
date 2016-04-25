import re
hand = open('mbox.txt')
regexpr = raw_input('Enter a regular expression: ')
count = 0
for line in hand:
    line = line.rstrip()
    x = re.findall(regexpr,line)
    if len(x) > 0:
        count = count + 1
print 'mbox.txt had', count, 'lines that matched', regexpr
