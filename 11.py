from tkinter import *


def register():
    with open('names.txt', 'a') as f:
        f.write(e1.get()+','+e2.get()+','+e3.get()+','+e4.get()+','+e5.get()+','+v.get())
        f.write('\n')


root = Tk()
root.config(bg='purple')
root.resizable(0, 0)

l1 = Label(root, text='Name', font=('times', 20), bg='purple', fg='yellow')
l1.grid(row=0, column=0)
e1 = Entry(root, font=('times', 20))
e1.focus_set()
e1.grid(row=0, column=1)

l2 = Label(root, text='Family', font=('times', 20), bg='purple', fg='yellow')
l2.grid(row=1, column=0)
e2 = Entry(root, font=('times', 20))
e2.grid(row=1, column=1)

l3 = Label(root, text='Birth Year', font=('times', 20), bg='purple', fg='yellow')
l3.grid(row=2, column=0)
e3 = Entry(root, font=('times', 20))
e3.grid(row=2, column=1)

l4 = Label(root, text='ID', font=('times', 20), bg='purple', fg='yellow')
l4.grid(row=0, column=2)
e4 = Entry(root, font=('times', 20))
e4.grid(row=0, column=3)

l5 = Label(root, text='Phone', font=('times', 20), bg='purple', fg='yellow')
l5.grid(row=1, column=2)
e5 = Entry(root, font=('times', 20))
e5.grid(row=1, column=3)
###########################################################################
l6 = Label(root, text='Sans', font=('times', 20), bg='purple', fg='yellow')
l6.grid(row=2, column=2)

v = StringVar()
r1 = Radiobutton(root, variable=v, bg='purple', text='Women', value='women', font=('times', 20))
r1.grid(row=2, column=3)
r1 = Radiobutton(root, variable=v, bg='purple', text='Men', value='men', font=('times', 20))
r1.grid(row=3, column=3)
##########################################################################
b1 = Button(root, text='Register', font=('times', 20),bg='purple',
            command=register)
b1.grid(row=4, column=0, columnspan=2)
b2 = Button(root, text='Cancel', font=('times', 20),bg='purple',
            command=root.destroy)
b2.grid(row=4, column=2, columnspan=2)

root.mainloop()
