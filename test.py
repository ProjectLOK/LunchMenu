from tkinter import *
import asyncio
root = Tk()
root.geometry('400x300')
l1 = Label(root, text='0')
l1.pack()

def main():
	l1.configure(text=str(int(l1.cget('text')) + 1))
	root.after(1000, main)

root.after(0, main)
root.mainloop())

asyncio.run(a())
print(1)
