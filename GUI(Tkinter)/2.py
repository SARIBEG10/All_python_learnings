import tkinter
""" CANVAS """

window = tkinter.Tk()
window.title('Canvas')
window.geometry("640x480-200-100")

canvas = tkinter.Canvas(window, width=400, height=400, bg='red', bd=4, relief='raised')
canvas.pack(side='top', anchor='ne')

# image = tkinter.PhotoImage(file='screen.png')
# canvas.create_image(50, 50, image=image)
# coordinates_arc = [60, 60, 200, 200]    # nimdayere shekl misaze
# canvas.create_arc(coordinates_arc, start=0, extent=180, fill='yellow')

# coordinates_oval = [80, 80, 200, 200]
# canvas.create_oval(coordinates_oval, fill='yellow')

# coordinates_poly = [0, 5, 200, 100, 0, 200]
# canvas.create_polygon(coordinates_poly, outline='yellow', fill='blue', width=5)

# coordinate_line = [150, 150, 200, 200]
# canvas.create_line(coordinate_line, fill='blue', width=10)

coordinates_poly = [100, 140, 110, 110, 100, 140, 110, 110, 100, 140, 110, 110, 100, 140, 110, 110]
canvas.create_polygon(coordinates_poly, outline='yellow', fill='blue', width=3)

window.mainloop()

