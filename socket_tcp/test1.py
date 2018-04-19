import socket
import time

PORT = 9999
HOST = ""
ADDR = (HOST, PORT)
CACHE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)
server.listen(3)

while True:
    client, addr = server.accept()
    print("连接到客户端：", addr)
    while True:
        data = client.recv(CACHE)
        data = data.decode()
        print("data:",data)
        if data == 'bye':
            break
        data = '[' + str(time.ctime()) + '] ' + data
        data = data.encode()
        client.send(data)
#server.close()
