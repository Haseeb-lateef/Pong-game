from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard





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
scoreboard = Scoreboard()
ball.speed("fastest")


#controls movement for left and right paddles
my_screen.listen()
my_screen.onkeypress(l_paddle.up, "w")
my_screen.onkeypress(l_paddle.down, "s")

my_screen.onkeypress(r_paddle.up, "Up")
my_screen.onkeypress(r_paddle.down, "Down")


game_on = True


while game_on:



    ball.float()

    if ball.detect_border():
        ball.bounce_y()

    ball.paddle_bounce(r_paddle,l_paddle)

    result = ball.out_of_bounds()

    if result == 1:
        scoreboard.r_score+=1
        scoreboard.update_score()
    elif result == 0:
        scoreboard.l_score+=1
        scoreboard.update_score()

    print(f"right score: {scoreboard.r_score}")
    print(f"left score: {scoreboard.l_score}")

    my_screen.update()
    print(ball.movement_speed)
    sleep(ball.movement_speed)




my_screen.exitonclick()






















