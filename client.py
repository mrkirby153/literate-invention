import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024
MESSAGE = "HELLO, WORLD!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send("PA$$W0RD".encode('utf-8'))

data = s.recv(BUFFER_SIZE).decode('utf-8')
if not data == "ok":
    print('Error: ', data)
    exit(1)
    
while 1:
    cmd = input("> ")
    if cmd == "exit":
        break
    s.send(cmd.encode('utf-8'))
    data = s.recv(BUFFER_SIZE).decode('utf-8')
    print(data)

s.close();