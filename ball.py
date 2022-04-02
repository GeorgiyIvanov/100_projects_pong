from turtle import Turtle
import random
FORWARD = 5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.reset_position()
        self.acceleration = 0

    def move(self):
        self.forward(FORWARD + self.acceleration)
        self.accelerate()

    def bounce_walls(self):
        self.setheading(360 - self.heading())

    def bounce_pads(self):
        self.setheading(180 + self.heading())

    def walls_collide(self):
        if self.ycor() > 290 or self.ycor() < -290:
            return True

    def reset_position(self):
        self.goto(0, 0)
        self.setheading(random.randint(0, 359))
        self.acceleration = 0

    def accelerate(self):
        self.acceleration += 0.005
