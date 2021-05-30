import socket                
  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)          
  
serveraddrport = ('127.0.0.1',12345)

while True:
    ip = str(input('Send the IP address:'))

    ip = ip.encode('utf-8');

    s.sendto(ip,serveraddrport)

    output = s.recvfrom(1024)
    
    print('MAC address is '+str(output[0].decode('utf-8')))

    s.close()    
    break    
