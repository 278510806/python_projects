import socket
import time

PORT = 9999
HOST = ""
ADDR = (HOST, PORT)
CACHE = 1024
'''
udp与tcp不同之处：
1.由于udp无连接状态，所以不需要socket.listen()
2.服务器等待客户端发送消息，接收到后直接返回data和客户端的地址
3.是由server与客户端通讯；而tcp是由server.accept获取到的连接socket进行通讯
'''

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

while True:
    data, addr = server.recvfrom(CACHE)
    data = data.decode()
    print("接收到客户端发来的数据",addr)
    data = "[" + time.ctime() + "]" + data
    data = data.encode()
    server.sendto(data,addr)
server.close()