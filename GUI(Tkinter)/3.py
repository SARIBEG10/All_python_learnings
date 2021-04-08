import tkinter
""" FRAMES IN TKINTER"""


window = tkinter.Tk()
window.title("frames in tkinter")
window.geometry("640x480-200-200")

# canvas = tkinter.Canvas(window, width=500, height=300, bd=5, bg='red')
# canvas.pack()
# frame = tkinter.Frame(canvas, height=50, width=100, relief='sunken')
# frame.pack(side='top', padx=5, pady=5)

frame = tkinter.Frame(window, width=300, height=300, bg='yellow')
frame.pack(side='top')

btn1 = tkinter.Button(frame, text='button1', fg='red')
btn1.pack(side='left')


btn2 = tkinter.Button(frame, text='button2', fg='blue')
btn2.pack(side='left')

btn3 = tkinter.Button(frame, text='button3', fg='green')
btn3.pack(side='right')



window.mainloop()





