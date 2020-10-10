from tkinter import *
from tkinter.ttk import Notebook

from data import i


def hesab(a, b, c):
    food['count'] = int(food_one.get())
    print(food)

def card(food):
    global food_one
    top = Toplevel(bg='#F2FD94')
    title = Label(top, text=food['name'], font=('times', 20, 'bold'))
    title.grid(row=0, column=0, sticky=W, padx=5, pady=5)

    r = '★'*food['rating']+str(food['rating']) + '(' + str(food['views']) + ')'
    rate = Label(top, text=r, fg='gray')
    rate.grid(row=1, column=0, sticky=W, padx=5, pady=5)

    description = Message(top, text=food['description'], bg='#FF8621', width=200)
    description.grid(row=2, column=0,columnspan=2)

    p = str(food['price'])+' IR Rial'
    price = Label(top, text=p, fg='blue')
    price.grid(row=3, column=0, sticky=W, padx=5)

    food_one = StringVar()
    food_one.trace('w', hesab)

    count = Spinbox(top, from_=0, to=100, width=2, textvariable=food_one)
    count.grid(row=3, column=1, padx=5, pady=5)


root = Tk()

note = Notebook()
note.grid(row=0, column=0)

food = Frame()
drink = Frame()
receipt = Frame()

note.add(food, text='Foods')
note.add(drink, text='Drinks')
note.add(receipt, text='Receipt')

# ################### Food1 ################### #
f = Frame(food)
f.grid(row=0, column=0)

img1 = PhotoImage(file=i['1']['img']).subsample(5)
l1 = Label(f, image=img1)
l1.grid(row=0, column=0)

b1 = Button(f, text='more...', bg='#007bff', fg='#ffffff', command=lambda: card(i['1']),
            activebackground='#0062CC', activeforeground='#ffffff')
b1.grid(row=1, column=0, sticky=W+E)

# ################### Food2 ################### #
f2 = Frame(food)
f2.grid(row=1, column=0)

img2 = PhotoImage(file=i['2']['img']).subsample(6)
l2 = Label(f2, image=img2)
l2.grid(row=0, column=0)

b2 = Button(f2, text='more...', bg='#007bff', fg='#ffffff', command=lambda: card(i['2']),
            activebackground='#0062CC', activeforeground='#ffffff')
b2.grid(row=1, column=0, sticky=W+E)
################################################

root.mainloop()
