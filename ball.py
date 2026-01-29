from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.shapesize(1,1)


    def float(self):
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.goto(x,y)

