from tkinter import *

def print_msg(entr):
    msg = entr.get()
    print(msg)

root = Tk()
root.title("Main")
entr = Entry(root)
b = Button(root, text = 'Print', command = lambda : print_msg(entr))
entr.pack()
b.pack()
root.mainloop()