from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
ball = Ball()
scoreboard = Scoreboard()

r_paddle = Paddle((270 , 0))
l_paddle = Paddle((-270 , 0))


screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 210 or ball.distance(l_paddle) < 50 and ball.xcor() < -210:
        ball.bounce_x()
    #Detect R paddle misses the ball
    if ball.xcor() > 280 :
        ball.reset_position()
        scoreboard.l_point()

    # Detect l paddle misses the ball
    if ball.xcor() < -280 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()