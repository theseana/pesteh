from tkinter import *

def start():
    print(e1.get())

root = Tk()
e1 = Entry(root, width=8)
e1.grid(row=2, column=0)

Button(root, text='Start', command=start).grid(row=3, column=0)
root.mainloop()