from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=1000,height=800)
screen.bgcolor("black")
screen.title("Ping Pong Game")
# to make movement smoother:
screen.tracer(0)

r_paddle = Paddle((450,0))
l_paddle = Paddle((-450,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

sleep_time = 0.1
game_on = True
while game_on:
    screen.update()
    # start moving the ball
    time.sleep(sleep_time)
    ball.goto(ball.xcor()+ball.x_move, ball.ycor()+ball.y_move)
    
    # handling collisions with upper and lower walls
    if ball.ycor() >= 380 or ball.ycor() <= -380:
        ball.y_move *= -1

    # handling collisions with ball and paddles
    if (ball.xcor() >= 430 and ball.distance(r_paddle)<=60) or (ball.xcor() <=-430 and ball.distance(l_paddle)<=60):
        ball.x_move *= -1
        sleep_time *= 0.8

    # if ball touches right boundary without touching the paddles
    if ball.xcor()  > 500:
        ball.goto(0,0)
        ball.x_move *= -1
        sleep_time = 0.1
        scoreboard.l_point()
    # if ball touches left boundary without touching the paddles
    if ball.xcor() < -500:
        ball.goto(0,0)
        ball.x_move *= -1
        sleep_time = 0.1
        scoreboard.r_point()

screen.exitonclick()