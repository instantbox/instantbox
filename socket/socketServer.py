from socket import *
import os

server_address = './uds_socket'

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise OSError


s = socket(AF_UNIX,SOCK_STREAM)

s.bind(server_address)


backlog = 1
s.listen(backlog)


conn, client_address = s.accept()


data = conn.recv(1024)


print("Connected by:",client_address)


print("Msg from client:",data.decode())


conn.send("Thank you:".encode()+data.upper())

# conn.close()
