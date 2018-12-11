from socket import *
 
s = socket(AF_UNIX,SOCK_STREAM)
server_address = './uds_socket'


s.connect(server_address)
 
sendMe=input("Enter your Msg:")

#通过send方法和recv方法通信。
#数据传递不能使用str类型，必须转化成二进制，“Hello”.encode()或b"Hello"

s.send(sendMe.encode())
data = s.recv(1024)

print("Received from serve:",data.decode())
 
s.close() 
