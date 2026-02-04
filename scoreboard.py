from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.divider()

        self.update_score()



    def update_score(self):
        self.clear()
        self.divider()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Impact", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Impact", 40, "normal"))


    def divider(self):
        self.goto(0, 300)
        self.pensize(5)

        self.setheading(270)  # face down

        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)



