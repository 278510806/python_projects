import socket

PORT=9999
HOST="localhost"
ADDR=(HOST,PORT)
CACHE=1024
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)

while True:
    data=input(">>")
    if not data:
        continue
    data=data.encode()
    client.send(data)
    data=client.recv(CACHE)
    data=data.decode()
    print(">>",data)
    if data=="bye":
        break
client.close()


