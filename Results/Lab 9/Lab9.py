from tkinter import *
import time



class TShape:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y


class TPoint (TShape):
    def __init__(self, x = 0.0, y= 0.0, width = 4.0):
        TShape.__init__(self, x, y)
        self.width = width


class Elips:
    def __init__(self, color = 'none', left_top = TPoint(10.0, 10.0), right_bottom = TPoint(90.0, 50.0)):
        self.left_top = left_top
        self.color = color
        self.right_bottom = right_bottom
        self.width = left_top.width
        self.pos_on_canvas = None

    def draw(self, canvas):
        if self.color == 'none':
            self.pos_on_canvas = canvas.create_oval(self.left_top.x, self.left_top.y, self.right_bottom.x, self.right_bottom.y, width = self.width)
        else:
            self.pos_on_canvas = canvas.create_oval(self.left_top.x, self.left_top.y, self.right_bottom.x, self.right_bottom.y, width = self.width, fill = self.color)

    def move(self, canvas, dest):
        x_mov = dest.x - canvas.coords(self.pos_on_canvas)[2]
        y_mov = dest.y - canvas.coords(self.pos_on_canvas)[3]
        canvas.move(self.pos_on_canvas, x_mov, y_mov)



class Round (Elips):
    def __init__(self, radius, color = 'none', center = TPoint(100.0, 100.0)):
        left_top = TPoint(center.x + radius, center.y + radius)
        right_bottom = TPoint(center.x - radius, center.y - radius)
        Elips.__init__(self, color, left_top, right_bottom)


class Sector (Elips):
    def __init__(self, startangle, angle, color = 'none', left_top = TPoint(10.0, 10.0), right_bottom = TPoint(100.0, 100.0)):
        self.angle = angle
        self.start_angle = startangle
        Elips.__init__(self, color, left_top, right_bottom)

    def draw(self, canvas):
        if self.color == 'none':
            self.pos_on_canvas = canvas.create_arc(self.left_top.x, self.left_top.y, self.right_bottom.x, self.right_bottom.y, start = self.start_angle, extent = self.angle, width = self.width)
        else:
            self.pos_on_canvas = canvas.create_arc(self.left_top.x, self.left_top.y, self.right_bottom.x, self.right_bottom.y, start = self.start_angle, extent = self.angle, fill = self.color, width = self.width)


aaa = Elips('red')
bbb = Round(10, 'red')
ccc = Sector(0, 90)
root = Tk()

c = Canvas(root, width=300, height=500, bg='white')
c.pack()

ccc.draw(c)
ccc.move(c, TPoint(190, 150))
ccc.move(c, TPoint(0, 0))

getshit = c.create_oval(10,10, 100,100, width = 1)

root.mainloop()