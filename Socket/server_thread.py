# Echo server program
import socket
import threading

def receive_data(conn, addr):
    global has_to_stop
    with conn:
        print('Connected by', addr)
        while True: # Read data until there is no more data
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()

            conn.sendall(data)  # Send back the data. Hence the "Echo" -name of the program.
            print(message)
            if message == 'stop' or message == 'q':
                #conn.close()
                #s.close() ei tarvita koska with sulkee s. ja conn.
                has_to_stop = True
                break

HOST = '172.20.4.61'        # Symbolic name meaning all available interfaces (''=0.0.0.0)
PORT = 65432              # Arbitrary non-privileged port (Ports >0 and <1024. Ports under 1024 need admin rights)
has_to_stop = False
socket.setdefaulttimeout(10)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # socket.AF_INET = Internet socket
    # socket.SOCK_STREAM = TCP (socket.SOCK_DGRAM = UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))    # Socket will be bind to HOST:PORT
    s.listen(1)             # Set socket in listen mode
    while not has_to_stop:
        print('waiting for connection')
        try:
            conn, addr = s.accept() # Start to accept connections. When a connection is stablished, a socket, address pair is returned
        except TimeoutError:

            continue # palauttaa kierroksen takaisin while not...:
        t = threading.Thread(target=receive_data, args=(conn, addr))
        t.start()
        #t.join() # ei tarvii odottaa koska..??

# The use of "with" is to avoid ".close()"