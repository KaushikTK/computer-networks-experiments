import socket                
  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)          
  
serveraddrport = ('127.0.0.1',12345)

while True:
    ip = str(input('Send something to the UDP server:'))

    ip = ip.encode('utf-8');

    s.sendto(ip,serveraddrport)

    if(str(ip.decode('utf-8')) == 'end'):
        break

    string = s.recvfrom(1024)

    string = string[0].decode('utf-8') 

    print('Client received : ' + str(string) + ' from UDP server')

s.close()        
