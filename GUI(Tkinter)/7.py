import tkinter
"""CHECKBOXES"""

window = tkinter.Tk()
window.title('checkboxes in labelframe')
window.geometry("1024x480")

label_frame = tkinter.LabelFrame(window, text='checkbox')
label_frame.grid(column=0, row=0)

var1 = tkinter.IntVar()
var1.set(1)
chk_btn = tkinter.Checkbutton(label_frame, text='sari', variable=var1)
chk_btn.grid(column=0, row=0, sticky='w')

var2 = tkinter.IntVar()
var2.set(0)
chk_btn2 = tkinter.Checkbutton(label_frame, text='ashot', variable=var2)
chk_btn2.grid(column=0, row=1, sticky='w')


window.mainloop()







