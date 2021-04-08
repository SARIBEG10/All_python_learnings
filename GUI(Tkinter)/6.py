import tkinter
"""TEXT WIDGET & ENTRY WIDGET"""

window = tkinter.Tk()
window.title('text and entry fields')
window.geometry("1024x480")
# text field / text widget inside the main widget
text = tkinter.Text(window, width=200, height=6, font=('arial', 20, 'bold'), fg='black')
text.focus()
text.pack()     # we can also use grid to place this widget
# entry field / entry widget inside the main widget
entry = tkinter.Entry(window, width=20, font=('arial', 30, 'italic'), fg='blue')
entry.pack(side='top', anchor='nw')     # we can also use grid to place this widget


window.mainloop()
