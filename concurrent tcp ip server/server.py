# this is server-side code
import socket
import time

s = socket.socket()          
print("Socket successfully created")
  
port = 12345                
  
s.bind(('127.0.0.1', port))         
print ('port:' + str(port))
  
s.listen(5)      
print ('socket is listening')            
  
while True: 

   c, addr = s.accept()  
   c.setblocking(False) # this is for concurrency
   print ('Got connection from' + str(addr)) 
  
   ip = c.recv(1024)
   ip = ip.decode('utf-8')

   if(ip == 'Please send the time and date information from the server..'):
          
      d_time = time.ctime()
      string = str(d_time)  
      c.send(string.encode('utf-8')) 
      c.close()



