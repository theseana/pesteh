from tkinter import *

def s():
    b1.config( state=DISABLED)

def d():
    pass
root = Tk()

b1 = Button(root, text='1', command=s)
b1.grid(row=0, column=0)
b2 = Button(root, text='2', command=d)
b2.grid(row=0, column=1)

root.mainloop()