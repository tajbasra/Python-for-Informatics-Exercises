fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
confidence = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence: '):
        count = count +1
        number = line.find(':')
        number = line[number+1:]
        confidence = confidence + float(number)
    count = float(count)
print 'Average spam confidence: ',confidence/count