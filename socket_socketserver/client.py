import socket
import os

PORT = 9999
HOST = "localhost"
ADDR = (HOST, PORT)
CACHE = 1024
'''
由于socketserver的xxxrequesthandler的默认处理方式是：1.接受连接；2.获取请求（并处理）；3.关闭连接；因此与其交互
每次都要重新连接
'''
while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    data = input(">>")
    if not data:
        print
        client.close()
        continue
    data = (data + os.linesep).encode()
    # data = data + os.linesep
    client.send(data)
    data = client.recv(CACHE)
    if not data:
        client.close()
        continue
    print(str(data))
    client.close()
