# Echo client program
import socket


HOST = '127.0.0.1'        # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        # Notice: Internet and TCP
    s.connect((HOST, PORT))     # Connect to remote port
    s.sendall(b'q')  # Send text. Notice that data is bytes
    data = s.recv(1024)         # Read back the echo

print('Received', repr(data))   # Print received data