import socket
from threading import Thread


clients = {}
address = {}

host = '127.0.0.1'
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def accept_client_connection():
    while True:
        client_conn, client_addr = s.accept()
        print("the" + str(client_addr) + " Has connected ")
        client_conn.send("Please enter your name to join chatroom ".encode('utf-8'))
        address[client_conn] = client_addr
        Thread(target=handle_client, args=(client_conn,)).start()


def broadcast(msg, prefix=""):
    for client in clients:
        client.send(bytes(prefix, 'utf-8') + msg)


def handle_client(conn):
    name = conn.recv(1024).decode('utf-8')
    welcome = name + " Welcome to sariclubhaouse"
    conn.send(bytes(welcome, 'utf8'))

    msg = name + " Has recently join to chatroom"
    broadcast(bytes(msg, 'utf-8'))
    clients[conn] = name
    while True:
        msg = conn.recv(1024)

        if msg != bytes('#quit', 'utf-8'):
            broadcast(msg, name + ":")

        else:
            conn.send(bytes('#quit', 'utf-8'))
            conn.close()
            del clients[conn]
            broadcast(bytes(name + " Has been left Chatroom", "utf-8"))


if __name__ == "__main__":

    s.listen(5)
    print("Sever is Up and Running")
    t1 = Thread(target=accept_client_connection)
    t1.start()
    t1.join()