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
        if self.ycor() > 220 :
            self.goto(self.xcor(), 225)

        else:
            y= self.ycor() +20
            self.goto(self.xcor(),y)



    def down(self):
        if self.ycor() < -220:
            self.goto(self.xcor(), -225)
        else:
            y= self.ycor() -20
            self.goto(self.xcor(),y)






