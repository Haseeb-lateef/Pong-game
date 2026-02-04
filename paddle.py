from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.start_pos = start_pos
        self.penup()
        self.goto(start_pos)
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.speed(1)

    def up(self):
        y= self.ycor() +20
        self.goto(self.xcor(),y)

    def down(self):
        y= self.ycor() -20
        self.goto(self.xcor(),y)






