word = 'banana'
letter = 'a'
def count(word,letter):
    count = 0

    for letter in word:
        if letter == 'a':
            count = count + 1
    return count
x=count(word,letter)
print x
    
#x = count(banana,a)
#print x

#word = 'banana'
#count = 0
#for letter in word:
#    if letter == 'a':
#        count = count + 1
#print count

#def addtwo(a,b):
#    added = a+b
#    return added

#x=addtwo(3,5)
#print x