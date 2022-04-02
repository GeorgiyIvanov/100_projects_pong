from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor('black')

screen.tracer(0)
left_paddle = Paddle(left=True)
right_paddle = Paddle(left=False)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    sleep(0.01)

    # Detect collision with the walls
    if ball.walls_collide():
        ball.bounce_walls()
    # Detect collision with the paddles
    if (ball.distance(left_paddle) < 50 and ball.xcor() < -350) or\
            (ball.distance(right_paddle) < 50 and ball.xcor() > 350):
        ball.bounce_pads()
    # Detect right miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    # Detect left miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
