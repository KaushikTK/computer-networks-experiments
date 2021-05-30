import socket                
  
s = socket.socket()          
  
port = 12345                
  
s.connect(('127.0.0.1', port)) 

ip = input('Enter the name of the file:')

ip = ip.encode('utf-8');

s.send(ip)

string = s.recv(1024)

string = string.decode('utf-8') 

if(string == 'not_present'):
    print('File not present')

else:
    print('Data present inside the file: '+ string)
    f = open('client_file.txt','w')
    f.write(string)
    f.close()
    print('File has been created at the client side')

s.close()