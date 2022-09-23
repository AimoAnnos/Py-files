from ast import arg
import socket
import threading

sem = threading.Semaphore() # varaa resurssin ettei 2 (tai useampi) voi muokata resurssia samaan aikaan -> crash

def broadcast(message: str, conn, addr)->  None:
    sem.acquire()
    for peer in connections.values():
        if peer['socket'] == conn:
            prefix = '[You]'
        else:
            prefix = peer['name']
        try:
            peer['socket'].sendall(f'{prefix} {message}'.encode())
        except:
            continue
    sem.release()

def manage_client(conn: socket, addr: tuple) -> None:
    global stopp
    with conn: # with sulkee yhteyden itse
        while not stopp:
            try:
                data = conn.recv(1024)
            except TimeoutError:
                continue
            if not data:
                break
            message = data.encode()
            if message.lower() == '\\quit':
                break
            elif message.lower() == '\\stop':
                break
            elif message.lower().startswith('\\name'):
                connections[addr]['name'] = f'[{message[6:]} <{addr[0]}:<{addr[1]}'
                continue
            elif message.lower() == '\\list':
                sem.acquire()
                for peer in connections.values():
                    conn.sendall(peer['name']).encode()
                    #conn.sendall(b'\n')
                sem.release()
                continue
            broadcast(message, conn, addr)
    sem.acquire()
    connections.pop(addr)
    sem.release()

HOST = '127.0.0.1'
PORT = 65432
stopp = False
connections = {}
socket.setdefaulttimeout(10)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # socket.AF_INET = Internet socket
    # socket.SOCK_STREAM = TCP (socket.SOCK_DGRAM = UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # define port as reusable so it can be bound again (in 1 min)
    s.bind((HOST, PORT))    # Socket will be bind to HOST:PORT
    s.listen()             # Set socket in listen mode
    while not stopp:
        try:
            conn, addr = s.accept()
        except TimeoutError:
            continue
        sem.acquire()
        connections[addr] = {'socket': conn, 'addr': addr , 'name': f'[Tuntematon<{addr[0]}:{addr[1]}>]'}
        sem.release()
        threading.Thread(target=manage_client, args=(conn,addr)).start()
        