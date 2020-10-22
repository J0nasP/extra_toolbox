from tkinter import *
import re

master = Tk()

lb = Listbox(master, selectmode=EXTENDED)
lb.pack()

lb.insert(END, "a list entry")

data = ["hej", "farvel"]
lb.delete(0, END) # clear

def insert():
    for ind, _ in enumerate(data):
        lb.insert(END, data[ind])

insert()

for i in lb.get(0,len(data)):
    print(i)


def findAmount(od, d="", c=1):
    d = od+" [{}]".format(str(c))
    return d if not d in data else findAmount(od, d, c+1)

current = 0

def select(event):
    global current
    current = lb.nearest(event.y)
    print("Current changed to", current)

def move(event):
    global current
    element = lb.nearest(event.y)
    try:
        if element != current:
            From = data[current]
            To = data[element]
            print("{} -> {}".format(From, To))
            data[current] = To
            data[element] = From
            lb.delete(0, len(data))
            insert()
            current = element
    except Exception as e: print(e)


lb.bind('<B1-Motion>', move)
lb.bind('<Button-1>', select)

def add():
    global data
    d = input("gib data: ")
    if d in data:
        d = findAmount(d)
    lb.delete(0, len(data))
    data += [d]
    insert()

Button(master, text="Add", command=lambda: add()).pack()

master.mainloop()