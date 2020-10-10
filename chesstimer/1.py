from threading import Thread
from time import sleep
from tkinter import *

def main():
    global left_timer, right_timer
    while True:
        sleep(1)
        if flag:
            left_timer = left_timer - 1
            m = int(left_timer / 60)
            s = left_timer % 60
            left['text'] = '{:02d}:{:02d}'.format(m, s)
        else:
            right_timer = right_timer - 1
            m = int(right_timer / 60)
            s = right_timer % 60
            right['text'] = '{:02d}:{:02d}'.format(m, s)

def s():
    t = Thread(target=main)
    t.start()


def stopl():
    global flag
    flag = False

def stopr():
    global flag
    flag = True


root = Tk()

# variables ##########################
left_timer = 1200
right_timer = 1200
flag = True
######################################

# Label ##############################
l1 = Label(root, text='Left Player',
           font=('times', 20, 'italic'))
l1.grid(row=0, column=0)

l2 = Label(root, text='Right Player',
           font=('times', 20, 'italic'))
l2.grid(row=0, column=1)
######################################

# Timer Label ########################
left = Label(root, text='20:00',
             font=('courier', 20))
left.grid(row=1, column=0)

right = Label(root, text='20:00',
              font=('courier', 20))
right.grid(row=1, column=1)
######################################

# Button #############################
b1 = Button(root,
            text='Stop',
            command=stopl,
            font=('courier', 20))
b1.grid(row=2, column=0)

b2 = Button(root,
            command=stopr,
            text='Stop',
            font=('courier', 20))
b2.grid(row=2, column=1)

b3 = Button(root,
            text='Start',
            command=s,
            font=('courier', 20))
b3.grid(row=3, column=0)

######################################

root.mainloop()