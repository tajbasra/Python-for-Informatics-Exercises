newlist = list()

while (True):
    number = raw_input('Enter a number: ')
    if number == 'done': break
    try:
        number = float(number)
    except:
        print 'I said enter a NUMBER!'
        continue
    newlist.append(number)

print 'Maximum: ', max(newlist)
print 'Minimum: ', min(newlist)
