
def middle():
    thinglist = list()
    while (True):
        inp = raw_input('Enter a thing: ')
        if inp == 'done': break
        thinglist.append(inp)
    newlist = thinglist[1:]
    newlist.remove(newlist[-1])
    print newlist

middle()