from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball((0, 0))
l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

keep_running = True
while keep_running:
    time.sleep(ball.current_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_top()

    if ball.distance(r_paddle) < 50 and ball.xcor() < -320 or ball.distance(l_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_sides()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
