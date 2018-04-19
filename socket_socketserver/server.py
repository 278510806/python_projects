import socketserver
import time

PORT = 9999
HOST = ""
ADDR = (HOST, PORT)


# 继承StreamRequestHandler表示使用tcp，udp使用DatagramRequesthandler
class MyRequestHandler(socketserver.StreamRequestHandler):
    '''
        处理器程序，用于接收请求和返回相应
        接受数据：self.rfile.readline()
        返回数据：self.wfile.write()
    '''


    def handle(self):
        data = self.rfile.readline()
        print("获取一个新的连接：", self.client_address)
        self.wfile.write(("[" + time.ctime() + "]" + str(data)).encode())


server = socketserver.TCPServer(ADDR, MyRequestHandler)
server.serve_forever()
