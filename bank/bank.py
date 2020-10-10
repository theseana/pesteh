from tkinter import *
from datetime import datetime


def turn():
    global n
    numbers.append(n + 1)
    n = n + 1
    dt = datetime.now()
    l1['text'] = dt.strftime("%b-%d-%Y")
    l2['text'] = dt.strftime("%H-%M-%S")
    l3['text'] = dt.strftime("%A")
    l4['text'] = numbers[-1]
    l5['text'] = 'remain: ' + str(len(numbers) - 1)

    txt ='{},{},{}'.format(l1['text'], l4['text'], l2['text'])
    with open('turn.txt', 'a') as file:
        file.write(txt)
        file.write('\n')


def op1():
    if numbers:
        lb2['text'] = numbers.pop(0)


def op2():
    if numbers:
        lb3['text'] = numbers.pop(0)


def op3():
    if numbers:
        lb4['text'] = numbers.pop(0)


root = Tk()

n = 0
numbers = []

l1 = Label(root, text='', font=('times', 20))
l1.grid(row=0, column=0)

l2 = Label(root, text='', font=('times', 20))
l2.grid(row=1, column=0)

l3 = Label(root, text='', font=('times', 20))
l3.grid(row=2, column=0)

l4 = Label(root, text='', font=('times', 20))
l4.grid(row=3, column=0)

l5 = Label(root, text='', font=('times', 20))
l5.grid(row=4, column=0)

b1 = Button(root, text='GetTurn!', command=turn, font=('times', 20))
b1.grid(row=5, column=0)

top = Toplevel(root)

b2 = Button(top, text='Operator1', command=op1, font=('times', 20))
b2.grid(row=0, column=0)
lb2 = Label(top, text='', font=('times', 20))
lb2.grid(row=1, column=0)

b3 = Button(top, text='Operator2', command=op2, font=('times', 20))
b3.grid(row=0, column=1)
lb3 = Label(top, text='', font=('times', 20))
lb3.grid(row=1, column=1)

b4 = Button(top, text='Operator3', command=op3, font=('times', 20))
b4.grid(row=0, column=2)
lb4 = Label(top, text='', font=('times', 20))
lb4.grid(row=1, column=2)

root.mainloop()
