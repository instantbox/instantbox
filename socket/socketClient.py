import time
from socket import *
import sys
import random
import string
import subprocess

s = socket(AF_UNIX,SOCK_STREAM)
server_address = './freeFile.sock'


s.connect(server_address)

def genString():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return salt

count = 0

while True:
    # sendMe = genString()

    sendMe = sys.stdin.readline()
    if sendMe == '':
        s.send('0000exit'.encode())
        break
    else:    
        print("发出数据: ", sendMe)
        s.send(sendMe.encode())

        # time.sleep(1)



s.close() 

