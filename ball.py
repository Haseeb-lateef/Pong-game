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
        self.move_x = 10
        self.move_y = 10



    def float(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def detect_border(self):

        if self.ycor() > 275 or self.ycor() < -275 :
            return True
        return False


    def bounce_back(self):

        if self.detect_border():
            self.move_y *=-1






