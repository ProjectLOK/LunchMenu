import time
from tkinter import *
from tkinter import ttk
import threading

root = Tk()
root.title('Diet')
main = ('Arial', 70)
small = ('Arial', 45)


def gui():
    frm = ttk.Frame(root, padding=20)
    date_today = ttk.Label(frm, text="daffafs", font=small)

    def display():
        date_today.grid(column=0, row=0)
        frm.pack(expand=YES, fill=BOTH)
        print("dis")

    def update():
        date_today.config(text="changed!")
        print("upd")

    display()
    time.sleep(5)
    update()
    root.mainloop()


gui()
