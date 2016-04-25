count = 0
total = 0
while True:
    try:
        line = raw_input('Enter a number: ')
        if line == 'done':
            break       
        line = float(line)
    except:
        print 'Bad number'
        continue

    count = count + 1
    total = total + line
    
print total, count, total/count