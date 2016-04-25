import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addressurl = raw_input('Enter the URL of a txt file:')

try:
    seperated = addressurl.split('/')
    url = seperated[2]
    request = 'GET ' + addressurl + ' HTTP/1.0\n\n'
    mysock.connect((url, 80))
    mysock.send(request)
    
    count = 0
    length = 0

    while True:
        data = mysock.recv(500)
        count += 1
        length += len(data)
        if ( len(data) < 1 ) :
            break
        if count <= 6:
            print data;
    mysock.close()
    print 'Total number of characters are:', length
except:
    print 'Webage cannot be opened'