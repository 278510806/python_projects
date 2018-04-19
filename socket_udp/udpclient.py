import socket
import time

PORT = 9999
HOST = "localhost"
ADDR = (HOST, PORT)
CACHE = 1024

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#udp无需向tcp一样建立连接，即：无需client.connect()方法

while  True:
    data=input(">>")
    if not data:
        continue
    data=data.encode()
    client.sendto(data,ADDR)
    data,addr=client.recvfrom(CACHE)
    print(data.decode())
client.close()
