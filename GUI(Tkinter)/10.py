import tkinter
from tkinter import simpledialog
"""DIALOG BOX"""


window = tkinter.Tk()
window.title('dialog box')
window.geometry("640x480")

# dialog = simpledialog.askstring("First box", "Whats your favourite player?")
dialog = simpledialog.askinteger("First box", "Whats your favourite number?")

if dialog is None:
    print("you don't have favourite number")

else:
    print('your favourite number is {}'.format(dialog))




window.mainloop()
































# for i in range(2, 7):
#     for x in range(2, i):
#         if i % x == 0:
#             print("the {} is composite".format(i))
#             break
#         else:
#             print("the {} is prime".format(i))





