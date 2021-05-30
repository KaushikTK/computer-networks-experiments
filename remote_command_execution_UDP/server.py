# import socket
# import subprocess
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host=socket.gethostname()
# port=1488
# s.bind((host,port))
# print('starting up on %s, port: %s' %(socket.gethostname(),port))

# while True:
#     data,addr = s.recvfrom(1024)
#     print("Requent: ",data.decode())
#     if(data.decode()=="exit"):
#         break
#     new_data=data.decode()
#     print(subprocess.getoutput(new_data))
#     msg4Cl=subprocess.getoutput(new_data)
#     s.sendto(msg4Cl.encode(), addr)
# s.close()


import socket                
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)          
print("Socket successfully created")
  
port = 12345                
  
s.bind(('', port))         
print ('port:' + str(port))
   
while True:

   data,addr = s.recvfrom(1024)
   data = data.decode('utf-8')

   output = subprocess.getoutput(data) # run the process in cmd

   s.sendto(output.encode('utf-8'),addr)
   s.close()
   break




