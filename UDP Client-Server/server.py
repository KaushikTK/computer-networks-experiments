import socket                
  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)          
print("Socket successfully created")
  
port = 12345                
  
s.bind(('', port))         
print ('port:' + str(port))
     
while True:

   ip = s.recvfrom(1024)

   msg = ip[0].decode('utf-8')
   addr = ip[1]
   print('UDP Server received : ' + str(msg) + ' from client')
   s.sendto(msg.encode('utf-8'),addr)

s.close()
