import tkinter
"""RADIO BUTTONS"""

window = tkinter.Tk()
window.title('radio buttons')
window.geometry("1024x480")

lframe = tkinter.LabelFrame(window, text='radio Buttons', fg='red')
lframe.grid(column=1, row=1)

r1 = tkinter.IntVar()
radio1 = tkinter.Radiobutton(lframe, text='Yes', variable=r1, value=1)
radio1.grid(column=0, row=0, sticky='w')
radio2 = tkinter.Radiobutton(lframe, text='No', variable=r1, value=2)
radio2.grid(column=0, row=1, sticky='w')

r2 = tkinter.IntVar()
white_btn = tkinter.Radiobutton(lframe, text='White', variable=r2, value=1)
white_btn.grid(column=0, row=2, sticky='w')
black_btn = tkinter.Radiobutton(lframe, text='Black', variable=r2, value=2)
black_btn.grid(column=0, row=3, sticky='w')


window.mainloop()
