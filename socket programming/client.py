
import socket                
  
s = socket.socket()          
  
port = 12345                
  
s.connect(('127.0.0.1', port)) 

a = input('Enter the first number:')
b = input('Enter the second number:')

ip = str(a) + '+' + str(b)

ip = ip.encode('utf-8');

s.send(ip)

string = s.recv(1024)

string = string.decode('utf-8') 

print(string)

s.close()        
