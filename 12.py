from tkinter import *

def avg():
    a = int(e1.get()) + int(e2.get()) + int(e3.get())
    a = a/3
    l4['text'] = a


root = Tk()

l1 = Label(root, text='Math')
l1.grid(row=0, column=0)

l2 = Label(root, text='Science')
l2.grid(row=1, column=0)

l3 = Label(root, text='History')
l3.grid(row=2, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)

e2 = Entry(root)
e2.grid(row=1, column=1)

e3 = Entry(root)
e3.grid(row=2, column=1)

l4 = Label(root, text='')
l4.grid(row=3, column=0)

b = Button(root, text='Avg', command=avg)
b.grid(row=4, column=0)

bc = Button(root, text='Cancel', command=root.destroy)
bc.grid(row=4, column=1)



root.mainloop()