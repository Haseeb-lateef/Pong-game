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


    def bounce_y(self):
        self.move_y *=-1

    def bounce_x(self):
        self.move_x  *=-1

    def paddle_bounce(self, r_paddle, l_paddle):

        if self.distance(r_paddle) < 50 and self.xcor() > 320:
            self.bounce_x()
        elif self.distance(l_paddle) < 50 and self.xcor() < -320:
            self.bounce_x()


    def out_of_bounds(self):

        if self.xcor() > 340:
            self.home()





