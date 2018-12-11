import time
from socket import *
import random
import string
import subprocess

s = socket(AF_UNIX,SOCK_STREAM)
server_address = './uds_socket'


s.connect(server_address)

def genString():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return salt

count = 0

while True:
    sendMe = genString()

    print("发出数据: ", sendMe)
    s.send(sendMe.encode())
    subprocess.check_output("echo {} >> ./dataSend.txt".format(sendMe), shell=True)

    time.sleep(1)

    # data = s.recv(1024)
    # if data == None:
    #     break
    # print("Received from serve:",data.decode())
    count += 1
    if count == 10:
        s.send('0000exit'.encode())

        break


s.close() 

