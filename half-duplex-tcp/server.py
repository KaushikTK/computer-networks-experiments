
import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('127.0.0.1', port))
print ('port:' + str(port))

s.listen()
print ('socket is listening')

c, addr = s.accept()
while True:

   ip = c.recv(1024)
   ip = ip.decode('utf-8')

   if(ip == 'end'):
    print('Ending the connection..')
    string = 'Ending the connection..'
    c.send(string.encode('utf-8'))
    c.close()
    break

   print('Message received from Client: ' + str(ip))
   #string = input('Server:')
   string = str(ip)
   c.send(string.encode('utf-8'))

