# this is client side code
import socket                
  
s = socket.socket()          
  
port = 12345                
  
s.connect(('127.0.0.1', port)) 

ip = 'Please send the time and date information from the server..'
print('The request sent is: '+ str(ip))

ip = ip.encode('utf-8');

s.send(ip)

string = s.recv(1024)

string = string.decode('utf-8') 

print('Time stamp received from server: '+ str(string))

s.close()        
