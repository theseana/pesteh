from tkinter import *


def enter():
    l2['text'] = e1.get()


root = Tk()

l1 = Label(root, text='WELCOME', font=('times', 30))
l1.pack()

l2 = Label(root, text='', font=('times', 30))
l2.pack()

e1 = Entry(root, font=('times', 20))
e1.pack()

b1 = Button(root, text='Enter', command=enter)
b1.pack()

root.mainloop()
