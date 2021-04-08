from tkinter import *
import tkinter
import socket
from threading import Thread


def recieve():
    while True:
        try:
            msg = s.recv(1024).decode('utf-8')
            listbox.insert(tkinter.END, msg)
        except:
            print("An Error occurred")


def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf-8"))
    if msg == '#quit':
        s.close()
        window.quit()


def on_closing():
    my_msg.set('#quit')
    send()


if __name__ == "__main__":

    window = Tk()
    window.configure(bg='green')
    window.title("SariClubhouse")

    chat_frame = Frame(window, width=15, bg='red')
    chat_frame.pack()

    my_msg = StringVar()
    my_msg.set("")

    scrool_bar = Scrollbar(chat_frame)
    listbox = Listbox(chat_frame, width=100, bg='red', yscrollcommand=scrool_bar.set)
    listbox.pack(side=RIGHT, fill=BOTH)
    scrool_bar.pack(side=LEFT, fill=Y)

    label = Label(window, text='Enter your message', font="Aerial", fg='blue', bg='green')
    label.pack()

    entry_field = Entry(window, textvariable=my_msg, fg='red', font='Aerial')
    entry_field.pack()

    send_button = Button(window, text='Send', font='Aerial', bg='green', fg='White', command=send)
    send_button.pack()

    quit_button = Button(window, text='Quit', font='Aerial', bg='green', fg='White', command=on_closing)
    quit_button.pack()

    host = 'localhost'
    port = 9090

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    recieve_thread = Thread(target=recieve)
    recieve_thread.start()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    mainloop()
