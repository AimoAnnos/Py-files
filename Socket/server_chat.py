import socket
import threading


sem = threading.Semaphore()

def broadcast(message: str, conn, addr) -> None:
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
    global has_to_stop
    with conn:
        while not has_to_stop:
            try:
                data = conn.recv(1024)
            except TimeoutError:
                continue
            if not data:
                break
            message = data.decode()
            if message.lower() == '\\quit':
                break
            elif message.lower() == '\\stop':
                has_to_stop = True
                break
            elif message.lower().startswith('\\name '):
                connections[addr]['name'] = f'[{message[6:]} <{addr[0]}:{addr[1]}>]'
                continue
            elif message.lower() == '\\list':
                sem.acquire()
                for peer in connections.values():
                    conn.sendall(peer['name'].encode())
                    #conn.sendall(b'\n')
                sem.release()
                continue
            broadcast(message, conn, addr)
    sem.acquire()
    connections.pop(addr)
    sem.release()

HOST = '127.0.0.1'
PORT = 65432
has_to_stop = False
connections = {}
socket.setdefaulttimeout(1)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Define the port as reusable (so it can be bound again)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    while not has_to_stop:
        try:
            conn, addr = s.accept()
        except TimeoutError:
            continue
        sem.acquire()
        connections[addr] = {'socket': conn, 'addr': addr, 'name': f'[Tuntematon <{addr[0]}:{addr[1]}>]'}
        sem.release()
        threading.Thread(target=manage_client, args=(conn, addr)).start()