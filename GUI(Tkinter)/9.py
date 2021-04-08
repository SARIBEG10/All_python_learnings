import tkinter
import sys
"""EVENTS IN TKINTER MODULE & BIND THE FUNCTION TO THE BUTTON"""

window = tkinter.Tk()
window.title('event handling')
window.geometry("640x480")

frame = tkinter.Frame(window, width=200, height=200, bd=2, relief='sunken')
frame.grid()

#
# def hello(event):
#     print("hello")
#     sys.exit()
#
#
# button = tkinter.Button(frame, text="SUBMIT")
# button.bind('<Button-1>', hello)
# button.grid(column=0, row=0)

firstname_label = tkinter.Label(frame, text='Firstname', fg='red')
firstname_label.grid(column=0, row=0)
lastname_label = tkinter.Label(frame, text='lastname', fg='blue')
lastname_label.grid(column=0, row=1)

fnam_var = tkinter.StringVar()
fnam_entry = tkinter.Entry(frame, width=10, textvariable=fnam_var)
fnam_entry.grid(column=1, row=0)

lnam_var = tkinter.StringVar()
lnam_entry = tkinter.Entry(frame, width=10, textvariable=lnam_var)
lnam_entry.grid(column=1, row=1)


def welcome():
    print("welcome mr/mrs: {} {}".format(fnam_entry.get(), lnam_entry.get()))
    sys.exit()


submit_button = tkinter.Button(frame, text="SUBMIT", command=welcome)
submit_button.grid(column=1, row=2)
window.mainloop()
