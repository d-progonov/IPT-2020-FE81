from lab9 import *
from tkinter import messagebox as mb
def reset(obj):
    for ob in obj:
        ob.delete()
        ob.set_default()
        ob.draw()


def main():
    root = Tk()
    c = Canvas(root, bg = 'white')
    c.pack(expand = YES, fill = BOTH)

    kv = Tkvadr(c, (10, 25 ), 'black', 5)
    trc = Trect(c, (50, 25), 'yellow', 5)
    trm = Tromb(c, (100, 25), 'red', 5)
    my_obj = [kv, trc, trm]

    sh = mb.showinfo(title = 'Info', message = 'Каждый квадрат совершает действие в соответствии с описанием его класса по сщелчку мыши')
    rest_b = Button(root, text = 'Reset', command = lambda my_obj = my_obj: reset(my_obj))
    rest_b.pack(side = LEFT, fill = X)

    for ob in my_obj:
        ob.draw()

    root.mainloop()
main()
