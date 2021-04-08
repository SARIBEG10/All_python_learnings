import tkinter
from tkinter import messagebox, simpledialog
"""MESSAGE BOXES"""

window = tkinter.Tk()
window.title('message boxes')
window.geometry("640x480")


def info_box():
    messagebox.showinfo("Info Box", "It's your tkinter module practice")


def warning_box():
    messagebox.showwarning("WARNING", "caution,It's dangerous")


def error_box():
    messagebox.showerror("Oooops!", "your password is wrong")


info_btn = tkinter.Button(window, text="Info", command=info_box)
info_btn.grid(column=0, row=0)

warning_btn = tkinter.Button(window, text="Warning", command=warning_box)
warning_btn.grid(column=1, row=0)

error_btn = tkinter.Button(window, text='Error', command=error_box)
error_btn.grid(column=2, row=0)


dialog = simpledialog.askstring('Favourite Food', "What's your favourite Food?")

if dialog is None:
    print("you must choose one food")
else:
    print(f"your favorite food is ", dialog)

window.mainloop()
