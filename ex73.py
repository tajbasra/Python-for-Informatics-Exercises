fname = raw_input('Enter the file name: ')
if fname == 'na na boo boo':
    print "NA NA BOO BOO TO YOU - You have been punk'd!"
    exit()
else:
    try:
        fhand = open(fname)
    except:
        print 'File cannot be opened:', fname
        exit()
    count = 0
    for line in fhand:
        line = line.rstrip()
        if line.startswith('Subject: '):
            count = count +1
print 'There were', count, 'subject lines in', fname