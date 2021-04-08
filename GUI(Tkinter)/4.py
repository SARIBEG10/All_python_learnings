import tkinter
"""ADD IMAGE TO FRAME AND CANVAS"""

window = tkinter.Tk()
window.title("add image to frame and canvas")
window.geometry("1024x840")

canvas = tkinter.Canvas(window, width=500, height=500, bg='yellow')
# frame = tkinter.Frame(window, width=300, height=300)
image = tkinter.PhotoImage(file='JADVAL.png')
# button = tkinter.Label(frame, image=image, text="CLICK ME")
button = tkinter.Button(canvas, image=image, text="CLICK ME")

# frame.pack(side='top')
canvas.pack()
button.pack()

window.mainloop()



