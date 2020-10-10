from tkinter import *

def cm():
    print('Ta-Da!')

root = Tk()

l = Label(root, text='First Name', font=('times', 15))
l.pack()
e = Entry(root, font=('times', 15))
e.pack()
l1 = Label(root, text='Last Name', font=('times', 15))
l1.pack()
e2 = Entry(root, font=('times', 15))
e2.pack()

b = Button(root, text='Set', command=cm, font=('times', 15))
b.pack()

root.mainloop()