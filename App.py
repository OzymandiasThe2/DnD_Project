from tkinter import *
from tkinter import messagebox

from dice_gen import dice_details


def cancel_app():
    quit()


class DNDMain:
    window = Tk()
    window.title('D&D Generator')
    window.geometry('250x250')
    menubar = Menu(window)
    window.config(menu=menubar)

    labe1 = Label(window, text="Welcome brave adventure.\nWhat is your request?")

    but1 = Button(window, text='Dice Rolls', bg="orange", fg="purple",)
    but2 = Button(window, text='Stat Gen', bg="orange", fg="purple")
    but3 = Button(window, text='Name Gen', bg="orange", fg="purple")
    but4 = Button(window, text='Monster Gen', bg="orange", fg="purple")
    but5 = Button(window, text='Loot Gen', bg="orange", fg="purple")
    but6 = Button(window, text='NPC Gen', bg="orange", fg="purple")
    but7 = Button(window, text='Exit Program', bg="orange", fg="purple", command=cancel_app)

    but1.grid(column=0, row=3)
    but2.grid(column=0, row=4)
    but3.grid(column=0, row=5)
    but4.grid(column=0, row=6)
    but5.grid(column=0, row=7)
    but6.grid(column=0, row=8)
    but7.grid(column=0, row=9)

    labe1.grid(column=0, row=0)

    operation_menu = Menu(menubar, tearoff=0)
    exit_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Exit", menu=exit_menu)
    exit_menu.add_command(label="Quit", command=window.quit)

    window.mainloop()
