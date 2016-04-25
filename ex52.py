count = 0
total = 0
smallest = None
largest = None
while True:
    try:
        line = raw_input('Enter a number: ')
        if line == 'done':
            break
        line = float(line)
    except:
        print 'Bad number'
        continue    
    if smallest is None or line < smallest:
        smallest = line
    if largest is None or line > largest:
        largest = line      
    line = float(line)


    count = count + 1
    total = total + line
    
print total, count, smallest, largest