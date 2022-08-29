from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1

    def up(self):
        turtle = self
        new_y = turtle.ycor() + MOVE_DISTANCE
        turtle.goto(turtle.xcor(), new_y)

    def reset_position(self):
        self.move_speed *= 0.9
        self.goto(STARTING_POSITION)
