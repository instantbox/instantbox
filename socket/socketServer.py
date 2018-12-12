from socket import *
import os
import subprocess

server_address = './freeFile.sock'

try:
    os.unlink(server_address)
    os.unlink("./data.txt")
except OSError:
    if os.path.exists(server_address):
        raise OSError

s = socket(AF_UNIX,SOCK_STREAM)

s.bind(server_address)

backlog = 1
s.listen(backlog)


while True:  

    connection, client_address = s.accept()

    while True:

        data = connection.recv(512)  

        if data.decode() == "0000exit":
            break
        else:
            print(data.decode())
            subprocess.check_output("echo \"{}\" >> ./data.txt".format(data.decode()), shell=True)
        # print("Connected by:",client_address)

        # print("Msg from client:",data.decode())

        # connection.send(data)
    print("close this connection")
    connection.close()
    break


