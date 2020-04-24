from tkinter import *
import random

class Location():
    def __init__(self, canvas, coords):
        self.coords = coords
        self.canvas = canvas

class Tpoint(Location):
    def __init__(self, canvas, coords, color, action = None):
        Location.__init__(self, canvas, coords)
        self.p_coords = self.get_point_coords()
        self.color = color
        self.pixel_size = 10
        self.id = self.canvas.create_rectangle(self.p_coords, fill = self.color, outline = self.color)
        self.action = action
        self.bind()
    def get_point_coords(self):
        x, y = self.coords
        return (x, y, x + 10, y + 10) ## pixel size == 10
    def draw(self):
        self.canvas.pack()
    def delete(self):
        self.canvas.delete(self.id)
    def bind(self):
        if self.action != None:
            self.canvas.tag_bind(self.id, '<Button-1>', self.action)

class Tkvadr(Tpoint):
    def __init__(self, canvas, coords, color, size):
        self.canvas = canvas
        self.coords = coords
        self.color = color
        self.size = size
        self.action = self.move
        self.points = []

    def create_points(self):
        x_ = self.coords[0]
        y_ = self.coords[1]
        for i in range(0, self.size):
            for k in range(0, self.size):
                coords_ = (x_, y_)
                self.points.append(Tpoint(self.canvas, coords_, self.color, self.action))
                x_ += 10
            x_ = self.coords[0]
            y_ += 10

    def draw(self):
        if len(self.points) == 0:
            self.create_points()
        for p in self.points:
            p.draw()
    def delete(self):
        for p in self.points:
            p.delete()
        self.points = []
    def move(self, event):
        new_x, new_y = random.randint(0, self.canvas.winfo_width() - 10), random.randint(0, self.canvas.winfo_height() - 10)
        self.coords = (new_x, new_y)
        self.delete()
        self.draw()
    def set_default(self):
        self.coords = (10, 10)
        self.color = 'blue'

class Trect(Tkvadr):
    def __init__(self, canvas, coords, color, size):
        Tkvadr.__init__(self, canvas, coords, color, size)
        self.action = self.move_change
        self.colors = ['black', 'yellow', 'red', 'blue', 'green']
    def move_change(self, event):
        self.color = random.choice(self.colors)
        self.move(event)
    def set_default(self):
        self.coords = (60, 10)
        self.size = 5
        self.color = 'yellow'

class Tromb(Trect):
    def __init__(self, canvas, coords, color, size):
        Trect.__init__(self, canvas, coords, color, size)
        self.action = self.super_move_change
    def super_move_change(self, event):
        self.size = random.randint(1, 15)
        self.move_change(event)
    def set_default(self):
        self.coords = (100, 10)
        self.size = 5
        self.color = 'red'
