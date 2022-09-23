import socket
import threading
import sys

def send_data():
    #global quittaa
    while True: # Read data until there is no more data
        message = input('send: ')
        message = bytes(message, "utf-8")
        if message == '\Quit':
            s.sendall(message)
            s.close()
            sys.exit()
        elif message == 'q':
            s.close()
            sys.exit()       
        s.sendall(message)
        #print(data.decode())

HOST = '95.217.212.162' # wifin ulkopuolelta
# HOST = '172.20.4.50'       
# HOST = '172.20.4.61'        # The remote host
PORT = 65432              # The same port as used by the server
socket.setdefaulttimeout(5)
quittaa = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    t = threading.Thread(target=send_data)
    t.start()
    while not quittaa:
        try:
            data = s.recv(1024)
            print(data.decode())
        except TimeoutError:
            continue
        if not data:
            break
        

