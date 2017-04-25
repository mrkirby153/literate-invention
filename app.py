import socket
import config
import subprocess

# Constants for TCP socket
BUFFER_SIZE = 1024


# Open the TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((config.TCP_HOST, config.TCP_PORT))
s.listen(1)
print('Listening on ', config.TCP_HOST, ':', config.TCP_PORT, sep='')


def send(data, response = False):
  conn.send(data.encode('utf-8'))
  if response:
    return conn.recv(BUFFER_SIZE).decode('utf-8')
  else:
    return None

def checkPassword(password):
  if not password:
    return False
  if not password == config.PASSWORD:
    print('Invalid password!')
    send('err_invalid_password')
    conn.close()
    return False
  send('ok')
  return True

def runCommand(command):
  # Run command and capture output
  output = subprocess.check_output(command.split(" ")).decode('utf-8')
  if not output:
    return "No Output"
  else:
    return output
while 1:
    conn, addr = s.accept()

    print('Connection from ', addr)
    password = conn.recv(BUFFER_SIZE).decode('utf-8')
    if not checkPassword(password):
      break
    print('Authenticated!')
    while 1:
        print('Waiting for command')
        data = conn.recv(BUFFER_SIZE).decode('utf-8')
        if not data:
          break
        print('Received command "', data, '"', sep="")
        output = subprocess.check_output(data.split(" ")).decode('utf-8')
        conn.send(output.encode('utf-8'))  # Echo back
    conn.close()
