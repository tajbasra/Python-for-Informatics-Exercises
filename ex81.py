
def chop():
    thinglist = list()
    while (True):
        inp = raw_input('Enter a thing: ')
        if inp == 'done': break
        thinglist.append(inp)
    del thinglist[0]
    x= thinglist.remove(thinglist[-1])
    print x

chop()