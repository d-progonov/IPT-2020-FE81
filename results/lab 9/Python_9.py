from tkinter import *
import time


class Location:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def draw(self, canvas):
        pass

    def change_all(self, canvas, offset):
        pass


class TPoint(Location):
    def __init__(self, x = 0.0, y = 0.0, width = 2.0):
        Location.__init__(self, x, y)
        self.width = width


class Line(Location):
    def __init__(self, color = 'blue', point_arr = None):
        if point_arr is None:
            point_arr = [TPoint(300, 10), TPoint(400.0, 100.0)]
        self.first_p = point_arr[0]
        self.color = color
        self.second_p = point_arr[-1]
        self.width = self.first_p.width
        self.line = None

    def draw(self, canvas):
        self.line = canvas.create_line(self.first_p.x, self.first_p.y, self.second_p.x, self.second_p.y, width=self.width, fill=self.color)

    def change_all(self, canvas, offset):
       canvas.coords(self.line, 300, 10, 350, 150)
       x_mov = offset.x - canvas.coords(self.line)[2]
       y_mov = offset.y - canvas.coords(self.line)[3]
       canvas.itemconfig(self.line, fill="red")
       canvas.move(self.line, x_mov, y_mov)


class PolyLine(Line):
    def __init__(self, color='blue', point_arr=None):
        if point_arr is None:
            point_arr = [TPoint(500, 10), TPoint(600.0, 100.0), TPoint(700.0, 100.0)]
        Line.__init__(self, color, point_arr)
        self.point_arr = point_arr.copy()
        self.color = color
        self.line = []

    def draw(self, canvas):
        prev = self.point_arr[0]
        for i in range(1, len(self.point_arr)):
            self.line.append(canvas.create_line(prev.x,
                                                         prev.y,
                                                         self.point_arr[i].x,
                                                         self.point_arr[i].y,
                                                         width=self.width,
                                                         fill=self.color))
            prev = self.point_arr[i]

    def change_all(self, canvas, offset):
        canvas.coords(self.line[0], 500, 10, 550, 150)
        canvas.coords(self.line[1], 550, 150, 650, 200)
        for line in self.line:
            canvas.itemconfig(line, fill="red")
            canvas.move(line, offset.x, offset.y)


class PolyGon(Line):
    def __init__(self, color='blue', point_arr=None):
        if point_arr is None or len(point_arr) < 5:
            point_arr = [TPoint(100.0, 100.0), TPoint(200.0, 100.0), TPoint(200.0, 200.0), TPoint(100.0, 200.0)]
        Line.__init__(self, color, point_arr)
        self.point_arr = point_arr.copy()
        self.line = []

    def draw(self, canvas):
        prev = self.point_arr[0]
        for i in range(1, 4):
            self.line.append(canvas.create_line(prev.x,
                                                         prev.y,
                                                         self.point_arr[i].x,
                                                         self.point_arr[i].y,
                                                         width=self.width,
                                                         fill=self.color))
            prev = self.point_arr[i]
        self.line.append(canvas.create_line(prev.x,
                                                     prev.y,
                                                     self.point_arr[0].x,
                                                     self.point_arr[0].y,
                                                     width=self.width,
                                                     fill=self.color))
    def change_all(self, canvas, offset):
        canvas.coords(self.line[0], 100, 100, 150, 150)
        canvas.coords(self.line[1], 150, 150, 100, 200)
        canvas.coords(self.line[2], 100, 200, 50, 150)
        canvas.coords(self.line[3], 50, 150, 100, 100)
        for line in self.line:
            canvas.itemconfig(line, fill="red")
            canvas.move(line, offset.x, offset.y)



root = Tk()
c = Canvas(root, width=950, height=500, bg='white')

line = Line()
polyline = PolyLine()
polygon = PolyGon()

line.draw(c)
polyline.draw(c)
polygon.draw(c)


def line_change():
    line.change_all(c, TPoint(600.0, 300.0))

def polyline_change():
    polyline.change_all(c, TPoint(300.0, 200.0))

def polygon_change():
    polygon.change_all(c, TPoint(600.0, 300.0))

b1 = Button(root, text="Change line", width=15, height=3, command=line_change)
b2 = Button(root, text="Change polyline", width=15, height=3, command=polyline_change)
b3 = Button(root, text="Change polygon", width=15, height=3, command=polygon_change)

c.pack()
b1.pack()
b2.pack()
b3.pack()

root.mainloop()
