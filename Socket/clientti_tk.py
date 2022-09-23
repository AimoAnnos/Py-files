import socket
import threading
import sys
import tkinter


def receive(s: socket) -> None:  # parametri -> palauttaa
    '''
    Receive and print messages from server
    '''
    global stopp
    while not stopp:
        try:        
            data = s.recv(1024)
        except TimeoutError:
            continue
        except:
            break
        if not data:
            # Palvelin sulkee yhteyden
            break
        msg_list.insert(tkinter.END, data.encode())
    stopp = True


def sender(s: socket) -> None:
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
        if message.lower() == '\\quit':
            break
    stopp = True
    send_ended = True
    while not receive_ended:
        pass

def send(event=None):
    message = my_msg.get()
    my_msg.set('')
    if message.lower() == 'exit': # hyväksyy myös capsit
        # käyttäjä sulkee yhteyden
        stopp = True
        top.quit()
    try:
        s.sendall(message.encode())
    except:
        stopp = True
        top.quit() 
    if message.lower() == '\\quit':
        stopp = True
        top.quit()
    
def on_closing(event=None):
    s.sendall(b'\\quit')
    top.quit()

top = tkinter.Tk()
top.title("Chat client")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar() # For the messages to be sent.
my_msg.set("Type here.")
scrollbar = tkinter.Scrollbar(messages_frame) # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

    
HOST = '95.217.212.162'
PORT = 65432

stopp = False
receive_ended = False
send_ended = False
socket.setdefaulttimeout(5)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except:
        print('Server not available')
        sys.exit()
    #s.sendall(b'\\Name Nimimerkki')
    threading.Thread(target=receive, args=(s,)).start() # args = tuple
    #sender(s)
    tkinter.mainloop()

    # t = threading.Thread(target=sender, args=(s,))
    # t.start() # args = tuple
    # receive(s)
