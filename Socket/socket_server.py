# Echo server program
import socket


HOST = '127.0.0.1'        # Symbolic name meaning all available interfaces (''=0.0.0.0)
PORT = 50007              # Arbitrary non-privileged port (Ports >0 and <1024. Ports under 1024 need admin rights)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # socket.AF_INET = Internet socket
    # socket.SOCK_STREAM = TCP (socket.SOCK_DGRAM = UDP)
    s.bind((HOST, PORT))    # Socket will be bind to HOST:PORT
    s.listen(1)             # Set socket in listen mode
    conn, addr = s.accept() # Start to accept connections. When a connection is stablished, a socket, address pair is returned
    with conn:
        print('Connected by', addr)
        while True: # Read data until there is no more data
            data = conn.recv(1024)
            if not data:
                break
            print(f'Received (and resending) {data}')
            conn.sendall(data)  # Send back the data. Hence the "Echo" -name of the program.

# The use of "with" is to avoid ".close()"