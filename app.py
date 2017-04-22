import socket

# Constants for TCP socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5555
BUFFER_SIZE = 1024

# Open the TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()

    print('Connection from ', addr)

    while 1:
        data = conn.recv(BUFFER_SIZE).decode('utf-8')
        if not data:
            break
        print('Received ', data)
        conn.send(data.encode('utf-8'))  # Echo back
    conn.close()
