import socket  
from os.path import exists              
  
s = socket.socket()          
print("Socket successfully created")
  
port = 12345                
  
s.bind(('', port))         
print ('port:' + str(port))
  
s.listen()      
print ('socket is listening')            
  
while True: 
  
   c, addr = s.accept()      
   print ('Got connection from' + str(addr)) 
  
   ip = c.recv(1024)
   ip = ip.decode('utf-8')

   if(exists(ip) == False):
      c.send('not_present'.encode('utf-8'))
   
   else:

      f = open(ip,'r')
      data = f.read()
      c.send(data.encode('utf-8')) 
   
   c.close()