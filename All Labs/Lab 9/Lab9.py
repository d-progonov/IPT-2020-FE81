'''
 * File: Lab9.py
 * Project: Python Labs
 * Variant: 20
 * Created Date: 10.05.20
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 
 '''

import turtle
from numpy import arange, pi, cos, sin, random

'''
 Some additional bloks of code
    - Own Exception;
    - Turtle-object to draw figures;
    - Functions to draw oval; 
'''
# # # # # # # # # # # # # # # # # # # # # # # # #
turtles = []
for i in range(0, 5):
    turtles.append(turtle.Turtle())
    turtles[i].shape("arrow")
    turtles[i].pencolor("black")
    turtles[i].fillcolor("black")
    turtles[i].shapesize(1,1,1)
    turtles[i].penup()

# # # # # # # # # # # # # # # # # # # # # # # # #

class TShape (object):
    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y)
        turtles[0].fillcolor("red")
        turtles[0].goto(self.x, self.x,)
        turtles[0].penup()

    def displayXY(self):
        print("X is:", self.x)
        print("Y is:", self.y, '\n')


class TPoint (TShape):
    def __init__(self, c):              # first call TPoint init           
        self.color = str(c)             # color of TPoint
        turtles[1].fillcolor(self.color)
        for dot in range(0, 40):        # draw 40 points with random coordinates
            turtles[1].goto(random.randint(-300, 300), random.randint(-300, 300))
            turtles[1].pen(pencolor=self.color, pensize=5, speed=8)
            turtles[1].dot(8); turtles[1].penup(); turtles[1].home()
        

class TEllipse (TPoint):
    def __init__(self, x, y, a, b, c):
        self.x = int(x) 
        self.y = int(y)
        self.color = c; self.a = a; self.b = b
        turtles[2].penup()
        turtles[2].goto(self.x, self.y)
        turtles[2].pendown()
        turtles[2].shape("circle")
        turtles[2].shapesize(self.a, self.b, 1)
        turtles[2].fillcolor(self.color); turtles[2].pencolor(self.color)
        turtles[2].penup()
    
    # Subsidiary Method to reset current shape
    def Del(self):
        turtles[2].goto(self.x, self.y)
        turtles[2].pendown(); turtles[2].shape("circle")
        del_color = "white"
        turtles[2].shapesize(self.a, self.b, 1)
        turtles[2].fillcolor(del_color)
        turtles[2].pencolor(del_color); turtles[2].pencolor(self.color)
        turtles[2].penup()

    def Move(self, newX, newY):
        # delete last ellipse  
        TEllipse.Del(self)
        turtles[2].penup()
        # create new ellipse
        self.x = newX; self.y = newY
        turtles[2].goto(self.x, self.y)
        turtles[2].pendown(); turtles[2].shape("circle") 
        turtles[2].shapesize(self.a, self.b, 1)
        turtles[2].fillcolor(self.color); turtles[2].pencolor(self.color)
        turtles[2].penup()
    
    def Rotate(self): 
        self.a, self.b = self.b, self.a         
        TEllipse.Move(self, self.x, self.y)


class TSector(TEllipse):
    def __init__(self, xpos, ypos, r, angle, c):
        self.xpos = xpos; self.ypos = ypos; self.color = c; self.R = r
        self.angle  = angle*pi / 180
        step = pi/180

        turtles[3].penup()
        turtles[3].setpos(self.xpos, self.ypos)
        turtles[3].color(self.color)
        turtles[3].begin_fill()
        turtles[3].pendown()

        for theta in arange(0, self.angle, step):
            turtles[3].setpos(self.xpos + self.R * cos(theta), self.ypos + self.R * sin(theta))

        turtles[3].setpos(self.xpos + self.R * cos(self.angle), self.ypos + self.R * sin(self.angle))
        turtles[3].setpos(self.xpos, self.ypos)
        turtles[3].end_fill()


# Bool variable to change Radius 
cR = False
class TRing(TEllipse):
    # Ring with External radius and Width
    def __init__(self, x, y, extR, w, c):
        self.x = x; self.y = y; self.width = w 
        self.color = c; self.extR = extR
        turtles[4].goto(self.x, self.y)
        turtles[4].down()
        turtles[4].width(self.width)
        turtles[4].color(self.color)
        turtles[4].circle(self.extR)

    def ChangeC(self, newC):
        self.color = newC
        turtles[4].down()
        turtles[4].width(self.width)
        turtles[4].color(self.color)
        if (cR == False): 
            turtles[4].circle(self.extR) 
    
    def ChangeR(self, newR):
        # Delete last ring with previous radius
        cR = True
        turtles[4].down()
        turtles[4].width(self.width)
        turtles[4].color("white")
        turtles[4].circle(self.extR)
        
        # Create new Ring with new Radius
        self.extR = newR
        TRing.ChangeC(self, self.color)
        cR = False
        

if __name__ == "__main__":
    T = TShape(50, 50)

    P = TPoint("red")
    E = TEllipse(10, 10, 4, 2, "red")

    E.Move(300, 300)
    E.Rotate()

    S = TSector(-100, 100, 100, 60, "green")
    
    R = TRing(100, 100, 100, 10, "red")
    R.ChangeC("blue")
    R.ChangeR(150)

    turtle.done()
