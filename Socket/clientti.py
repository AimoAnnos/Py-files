from ast import arg
import socket
import threading
import sys
import argparse

from parso import parse


def receive(s: socket) -> None:  # parametri -> palauttaa
    '''
    Receive and print messages from server
    '''
    global stopp
    global receive_ended
    while not stopp:
        try:        
            data = s.recv(1024)
        except TimeoutError:
            continue
        except:
            stopp = True
            break
        if not data:
            # Palvelin sulkee yhteyden
            stopp = True
            break
        print(data.decode())
    stopp = True
    receive_ended = True
    while not send_ended:
        pass

def send(s: socket) -> None:
    '''
    Ask user for input and send to server
    '''
    global stopp # globaaliksi että muuttujan arvoa voi muuttaa
    global send_ended
    while not stopp:
        message = input('send:' )
        if message.lower() == 'exit': # hyväksyy myös capsit
            # käyttäjä sulkee yhteyden
            break
        try:
            s.sendall(message.encode())
        except:
            break 
        if message.lower() == '\\quit' or message.lower() == '\\stop':
            break
    stopp = True
    send_ended = True
    while not receive_ended:
        pass

# parser = argparse.ArgumentParser(description='chat client')

# #parser.add_argument('ip', help='IP address of the server')
# parser.add_argument('--local', action='store_true', help='Use local chat server')

# args = parser.parse_args()

#HOST = '95.217.212.162'
HOST = '127.0.0.1'
# if args.local:
#     HOST = '127.0.0.1'
PORT = 65432

stopp = False
receive_ended = False
send_ended = False
socket.setdefaulttimeout(8)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except:
        print('Server not available')
        sys.exit()
    #s.sendall(b'\\Name Nimimerkki')
    # threading.Thread(target=receive, args=(s,)).start() # args = tuple
    # send(s)

    t = threading.Thread(target=send, args=(s,))
    t.start() # args = tuple
    receive(s)
