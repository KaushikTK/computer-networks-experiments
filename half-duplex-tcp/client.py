import socket

s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

while True:
    ip = input('Please enter your message: ')

    ip = ip.encode('utf-8');

    s.send(ip)

    string = s.recv(1024)

    string = string.decode('utf-8')

    if(string == 'Ending the connection..'):
        print(string)
        s.close()
        break

    print('Message received from Server: ' + string)

