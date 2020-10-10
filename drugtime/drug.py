from threading import Thread
from time import sleep
from tkinter import *


def time_format(seconds):
    m = int(seconds/60)
    s = seconds % 60
    return '{:02d}:{:02d}'.format(m, s)


# input str '01:15: >>> output int 75
def get_seconds(s):
    t = s.split(":")
    return int(t[0])*60 + int(t[1])


def counter(label, seconds, button):
    while seconds:
        sleep(1)
        seconds -= 1
        label['text'] = time_format(seconds)
    button.config(state=ACTIVE)


def start(button):
    if button == '1':
        b1.config(state=DISABLED)
        t1['text'] = e1.get()
        second1 = get_seconds(e1.get())
        th1 = Thread(target=counter, args=(t1, second1, b1))
        th1.start()
    elif button == '2':
        b2.config(state=DISABLED)
        t2['text'] = e2.get()
        second2 = get_seconds(e2.get())
        th2 = Thread(target=counter, args=(t2, second2, b2))
        th2.start()
    elif button == '3':
        b3.config(state=DISABLED)
        t3['text'] = e3.get()
        second3 = get_seconds(e3.get())
        th3 = Thread(target=counter, args=(t3, second3, b3))
        th3.start()


root = Tk()

# Row 0 - Label Name
Label(root, text='Patient1').grid(row=0, column=0)
Label(root, text='Patient2').grid(row=0, column=1)
Label(root, text='Patient3').grid(row=0, column=2)

# Row 1 - Label Time
t1 = Label(root, text='00:00')
t1.grid(row=1, column=0)
t2 = Label(root, text='00:00')
t2.grid(row=1, column=1)
t3 = Label(root, text='00:00')
t3.grid(row=1, column=2)

# Row 2 - Entry Time
e1 = Entry(root, width=6)
e1.grid(row=2, column=0)
e2 = Entry(root, width=6)
e2.grid(row=2, column=1)
e3 = Entry(root, width=6)
e3.grid(row=2, column=2)

# Row 3 - Button Star
b1 = Button(root, text='Start', command=lambda: start('1'))
b1.grid(row=3, column=0)
b2 = Button(root, text='Start', command=lambda: start('2'))
b2.grid(row=3, column=1)
b3 = Button(root, text='Start', command=lambda: start('3'))
b3.grid(row=3, column=2)

root.mainloop()