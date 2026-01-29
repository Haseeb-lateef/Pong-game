from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep


#screen set up
my_screen = Screen()
my_screen.setup(800,600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)


#creates paddles
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()



#controls movement for left and right paddles
my_screen.listen()
my_screen.onkey(l_paddle.up, "w")
my_screen.onkey(l_paddle.down, "s")

my_screen.onkey(r_paddle.up, "Up")
my_screen.onkey(r_paddle.down, "Down")


game_on = True


while game_on:

    ball.float()
    my_screen.update()
    sleep(0.1)




my_screen.exitonclick()






















