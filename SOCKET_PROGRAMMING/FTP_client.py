import socket

host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
filename = 'sari.txt'
s.send(filename.encode())
file = s.recv(1024)
print(file.decode())
s.close()










