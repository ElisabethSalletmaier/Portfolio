from turtle import Screen
from classes import Paddle, Scoreboard, Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)    # turns off animation (e.g. turtle going to first position)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
"""moving the paddles with buttons"""
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    """collision with wall top and bottom"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    """collision with paddle"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    """detect right paddle misses"""
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    """detect left paddle misses"""
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()