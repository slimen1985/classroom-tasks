import socket

sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_server.bind(('127.0.0.1', 8888))

while True:
    try:
        result = sock_server.recv(1024)
    except KeyboardInterrupt:
        sock_server.close()
        break
    else:
        print('Message: ', result.decode('utf-8'))

