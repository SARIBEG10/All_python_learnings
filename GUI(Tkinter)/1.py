import tkinter
"""LABEL-IMAGE-BUTTON-ICONBITMAP"""
window = tkinter.Tk()
window.title("My First Gui")
window.geometry("640x480")
# window.config(bg='red')
# image = tkinter.PhotoImage(file='screen.png')
# button = tkinter.Button(window, image=image)
# button.pack()
textlabel = tkinter.Label(window, text='Saribeg', font=("Arial Bold", 60))
textlabel.grid(column=0, row=0)
button = tkinter.Button(window, text='submit', bg='red', fg='yellow')
button.grid(column=1, row=0)

window.mainloop()