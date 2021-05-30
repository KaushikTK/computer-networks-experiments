import socket                
import threading

s = socket.socket()          
  
port = 12345                
  
s.connect(('127.0.0.1', port)) 

def get_data(c):
    ip = c.recv(1024)
    ip = ip.decode('utf-8')
    print(str(ip))
    get_data(c)
    
def send_data(c):
    ip = input()
    c.send(ip.encode('utf-8'))
    send_data(c)

def start_sending():
    ts = threading.Thread(target=send_data, args=(s,))
    ts.start()

def start_recv():
    tr = threading.Thread(target=get_data, args=(s,))
    tr.start()


start_sending()
start_recv()
