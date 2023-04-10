from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_is_on = True

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game by Szabi")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        # Bounce of the wall
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss and reset position
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()


    # Detect left paddle miss and reset position
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()



































screen.exitonclick()
