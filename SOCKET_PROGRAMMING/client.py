import socket

serveraddress = ('localhost', 8080)

s = socket.socket()
s.connect(serveraddress)
message = s.recv(1024)

while message:
    print("Message : ", message.decode())
    message = s.recv(1024)

s.close()
