import tkinter

# keys = [[('CE', 1), ('C', 1)],
#         [('7', 1), ('8', 1), ('9', 1)],
#         [('4', 1), ('5', 1), ('6', 1)],
#         [('3', 1), ('2', 1), ('1', 1)], ]


def press(num):
    global equal
    equal = equal + str(num)
    entry_filed.set(equal)


def equalpress():
    try:
        global equal
        result = eval(equal)
        entry_filed.set(result)

        equal = ""
    except Exception:
        entry_filed.set("Invalid entry")
        equal = ""


def clear():
    global equal
    equal = ""
    entry_filed.set("")


if __name__ == "__main__":
    window = tkinter.Tk()
    equal = ""
    frame = tkinter.Frame(window)
    frame.grid(column=0, row=1)

    entry_filed = tkinter.StringVar()
    entry = tkinter.Entry(window, width=15, fg='blue', textvariable=entry_filed)
    entry.grid(column=0, row=0, sticky='nsew', columnspan=3)

    button0 = tkinter.Button(frame, width=2, height=1, text='0', command=lambda: press(0)).grid(column=0, row=0,
                                                                                                sticky='e')
    button1 = tkinter.Button(frame, width=2, height=1, text='1', command=lambda: press(1)).grid(column=0, row=1,
                                                                                                sticky='e')
    button2 = tkinter.Button(frame, width=2, height=1, text='2', command=lambda: press(2)).grid(column=0, row=2,
                                                                                                sticky='e')
    button3 = tkinter.Button(frame, width=2, height=1, text='3', command=lambda: press(3)).grid(column=0, row=3,
                                                                                                sticky='e')
    button4 = tkinter.Button(frame, width=2, height=1, text='4', command=lambda: press(4)).grid(column=1, row=0,
                                                                                                sticky='e')
    button5 = tkinter.Button(frame, width=2, height=1, text='5', command=lambda: press(5)).grid(column=1, row=1,
                                                                                                sticky='e')
    button6 = tkinter.Button(frame, width=2, height=1, text='6', command=lambda: press(6)).grid(column=1, row=2,
                                                                                                sticky='e')
    button7 = tkinter.Button(frame, width=2, height=1, text='7', command=lambda: press(7)).grid(column=1, row=3,
                                                                                                sticky='e')
    button8 = tkinter.Button(frame, width=2, height=1, text='8', command=lambda: press(8)).grid(column=2, row=0,
                                                                                                sticky='e')
    button9 = tkinter.Button(frame, width=2, height=1, text='9', command=lambda: press(9)).grid(column=2, row=1, sticky='e')

    add_button = tkinter.Button(frame, width=2, height=1, text='+', command=lambda: press('+')).grid(column=2, row=3, sticky='e')

    minus_button = tkinter.Button(frame, width=2, height=1, text='-', command=lambda: press('-')).grid(column=2, row=4, sticky='e')

    divison_button = tkinter.Button(frame, width=2, height=1, text='/', command=lambda: press('/')).grid(column=1, row=4, sticky='e')

    multiply_button = tkinter.Button(frame, width=2, height=1, text='*', command=lambda: press('*')).grid(column=0, row=4,sticky='e')

    clear_button = tkinter.Button(frame, width=2, height=1, text='C', command=clear).grid(column=0, row=5, sticky='e')
    equal_button = tkinter.Button(frame, width=2, height=1, text='=', command=equalpress).grid(column=2, row=2, sticky='e')

# row = 0
    # for k in keys:
    #     col = 0
    #     for x in k:
    #         buttons = tkinter.Button(frame, width=x[1], height=x[1], text=x[0])
    #         buttons.grid(column=col, row=row)
    #         row += 1
    #     col += 1

    window.mainloop()
