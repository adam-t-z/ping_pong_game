"""
Ping Pong Game
==============
This is a classic two-player ping pong game implemented using the `turtle` module. 
Players control paddles on either side of the screen to hit a ball back and forth. 
Points are scored when the ball crosses a player's boundary.

Key Controls:
- Right paddle (Player 1): Move up using the "Up" arrow key, move down using the "Down" arrow key.
- Left paddle (Player 2): Move up using the "W" key, move down using the "S" key.

Modules:
- `paddle.py`: Defines the Paddle class for controlling the paddles.
- `ball.py`: Defines the Ball class for controlling the ball's movement and collision logic.
- `score.py`: Defines the ScoreBoard class for tracking and displaying scores.
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

# Set up the screen
screen = Screen()
screen.setup(width=1000, height=800)  # Screen dimensions
screen.bgcolor("black")               # Background color
screen.title("Ping Pong Game")        # Title of the window
screen.tracer(0)                      # Disable automatic screen updates for smoother animation

# Create game objects
r_paddle = Paddle((450, 0))           # Right paddle (Player 1)
l_paddle = Paddle((-450, 0))          # Left paddle (Player 2)
ball = Ball()                         # Ball object for movement and collisions
scoreboard = ScoreBoard()             # Scoreboard to track player scores

# Set up key listeners for paddle movements
screen.listen()
screen.onkey(r_paddle.go_up, "Up")    # Right paddle moves up
screen.onkey(r_paddle.go_down, "Down")  # Right paddle moves down
screen.onkey(l_paddle.go_up, "w")     # Left paddle moves up
screen.onkey(l_paddle.go_down, "s")   # Left paddle moves down

# Initialize game variables
sleep_time = 0.1  # Delay for ball movement, decreases as game progresses
game_on = True    # Main game loop flag

# Game loop
while game_on:
    screen.update()  # Update the screen for smooth animation
    time.sleep(sleep_time)  # Control game speed

    # Move the ball
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

    # Collision with the top and bottom walls
    if ball.ycor() >= 380 or ball.ycor() <= -380:
        ball.y_move *= -1  # Reverse ball's vertical direction

    # Collision with paddles
    if (ball.xcor() >= 430 and ball.distance(r_paddle) <= 60) or (ball.xcor() <= -430 and ball.distance(l_paddle) <= 60):
        ball.x_move *= -1  # Reverse ball's horizontal direction
        sleep_time *= 0.8  # Increase speed for a more challenging game

    # Ball misses the right paddle
    if ball.xcor() > 500:
        ball.goto(0, 0)   # Reset ball position to center
        ball.x_move *= -1  # Reverse direction
        sleep_time = 0.1  # Reset speed
        scoreboard.l_point()  # Increment left player's score

    # Ball misses the left paddle
    if ball.xcor() < -500:
        ball.goto(0, 0)   # Reset ball position to center
        ball.x_move *= -1  # Reverse direction
        sleep_time = 0.1  # Reset speed
        scoreboard.r_point()  # Increment right player's score

# Exit the game on mouse click
screen.exitonclick()
