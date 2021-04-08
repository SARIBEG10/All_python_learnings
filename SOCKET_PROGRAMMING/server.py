import socket


host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("Server is up and running")
con, address = s.accept()
print("The connection has been established for {}, {}".format(str(address), str(con)))
con.send("the first message from the server".encode())
con.close()
