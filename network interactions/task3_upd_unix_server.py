import os
import sys
import socket
if sys.platform == 'win32':
    from socket import AF_INET as AF_UNIX
else:
    from socket import AF_UNIX

unix_socket_name = 'unix.sock'

sock = socket.socket(AF_UNIX, socket.SOCK_DGRAM)

try:
    if os.path.exists(unix_socket_name):
        os.unlink(unix_socket_name)
except OSError:
    print(f"Failed to remove {unix_socket_name}")

sock.bind((unix_socket_name,))

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message: ', result.decode('utf-8'))