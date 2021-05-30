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

   cmd = 'arp /a ' + data
   output = subprocess.getoutput(cmd) # run the process in cmd

   if(output == 'No ARP Entries Found.'):
      output = 'No ARP Entries Found'
      s.sendto(output.encode('utf-8'),addr)
   
   else:
         output = output.split('\n')[3] 
         output = output.strip()
         output = " ".join(output.split())
         output = output.split()[1]
         s.sendto(output.encode('utf-8'),addr)

   s.close()
   break




