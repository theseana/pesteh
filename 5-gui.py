from tkinter import *

root = Tk()
root.config(bg='yellow')

l1 = Label(root, text='Hello World!', bg='magenta')
l1.pack(side=LEFT)

b1 = Button(root, text='Click Me Please!', bg='cyan')
b1.pack(side=LEFT)

l2 = Label(root, text='Ta-Da!', bg='green')
l2.pack(side=LEFT)

root.mainloop()
