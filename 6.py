from tkinter import * 
import turtle

def change():
    # root['bg'] = a.get()
    turtle.color(a.get())
    turtle.circle(100)
    turtle.done()

root = Tk()
a = Entry(root)
a.pack()
b = Button(root, text='Change', command=change)
b.pack()
root.mainloop()