# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host = socket.gethostname()
# port=1488
# s.connect((host,port))
# print("connected to the server:",host)
# while True:
#     m=input(str("Command: "))	
#     s.sendto(m.encode(),(host,port))
#     if(m=="exit"):
#         break;
#     msgFromServ = s.recvfrom(1024)
#     msg = "Output: {}".format(msgFromServ[0].decode())
#     print(msg)
# s.close()


import socket                
  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)          
  
serveraddrport = ('127.0.0.1',12345)

while True:
    ip = str(input('Send something to the UDP server:'))

    ip = ip.encode('utf-8');

    s.sendto(ip,serveraddrport)

    output = s.recvfrom(1024)

    print(str(output[0].decode('utf-8')))

    s.close()    
    break    
