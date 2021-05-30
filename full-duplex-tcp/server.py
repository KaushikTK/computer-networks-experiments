import threading
import socket                
  
s = socket.socket()         
port = 12345                
  
s.bind(('', port))         
print ('port:' + str(port))
  
s.listen()      
print ('socket is listening')            


def send_data(c):
    res = input()
    c.send(res.encode('utf-8'))
    send_data(c)
    

def get_data(c):
    req = c.recv(1024)
    req = req.decode('utf-8')
    print(str(req))
    get_data(c)

def start_send(con):
    ts = threading.Thread(target=send_data, args=(con,))       
    ts.start()


def start_recv(con):
    tr = threading.Thread(target=get_data, args=(con,))
    tr.start()


con, addr = s.accept()
start_send(con)
start_recv(con)
