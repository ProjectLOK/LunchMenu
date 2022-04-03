import time
from tkinter import *
from tkinter import ttk
from scripts.lunch_api import lunch_api
import threading



"""class WorkThread(threading, Thread):
    def __init__(self, menu):
        threading.Thread.__init__(self)
        """


root = Tk()
root.title('Diet')
main = ('Arial', 70)
small = ('Arial', 45)
lunch = lunch_api()
menu1 = StringVar()
menu1.set(lunch.dish[0])
root.update_idletasks()

frm = ttk.Frame(root, padding=20)
date_today = ttk.Label(frm, text=lunch.date[0], font=small)
date_next = ttk.Label(frm, text=lunch.date[1], font=small)
dish_today = ttk.Label(frm, textvariable=menu1, padding=10, font=main, anchor=N)
dish_next = ttk.Label(frm, text=lunch.dish[1], padding=10, font=main, anchor=N)

def display():
    date_today.grid(column=0, row=0)
    date_next.grid(column=2, row=0)
    dish_today.grid(column=0, row=1)
    dish_next.grid(column=2, row=1)
    ttk.Label(frm, text='>', padding=10, font=main, anchor=N).grid(column=1, row=1)
    frm.pack(expand=YES, fill=BOTH)

def update():
    lunch = lunch_api()
    menu1.set(lunch.dish[0])
    root.update_idletasks()

    print("api call")


while True:
    update()
"""
def loop():
    while True:
        
t = threading.Timer(10, update)

t.start()

loop()
root.mainloop()

"""