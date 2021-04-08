import tkinter
"""CANVAS ALWAYS PLACED INSIDE FRAME"""

window = tkinter.Tk()
window.title("canvas inside the frame")
window.geometry('1024x480')

frame = tkinter.Frame(window, width=500, height=500, bd=2, relief='sunken', bg='red')
canvas = tkinter.Canvas(frame, width=500, height=500, bd=1, bg='green')
canvas.create_text(250, 20, text='canvas always inside the frame', font=('arial', 10, 'bold', 'italic'))

canvas.pack()
frame.pack()
window.mainloop()
