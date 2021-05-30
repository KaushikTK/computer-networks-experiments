import socket                
  
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
   ip = ip.split('+')
   ans = 0
   for i in ip:
    ans += int(i)
  
   string = 'The sum of ' + str(ip[0]) + ' and ' + str(ip[1]) + 'is ' + str(ans)  
   c.send(string.encode('utf-8')) 
  
   c.close()