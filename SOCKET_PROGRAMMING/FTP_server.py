import socket

host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
con, address = s.accept()
try:
    filname = con.recv(1024)
    file = open(filname, 'rb')
    readfile = file.read()
    con.send(readfile)
    file.close()
    con.close()
except:
    con.send("File has not been found".encode())


