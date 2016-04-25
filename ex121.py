import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addressurl = raw_input('Enter the URL of a txt file:')

try:
    seperated = addressurl.split('/')
    url = seperated[2]
    request = 'GET ' + addressurl + ' HTTP/1.0\n\n'
    mysock.connect((url, 80))
    mysock.send(request)


    while True:
        data = mysock.recv(512)
        if ( len(data) < 1 ) :
            break
        print data;

    mysock.close()
except:
    print 'Webage cannot be opened'