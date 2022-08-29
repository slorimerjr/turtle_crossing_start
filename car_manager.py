from turtle import Turtle
import random
from random import randint

# Create cars that are 20px high by 40px wide that are randomly generated along the
# y-axis and move to the left edge of the screen. No cars should be generated in the
# top and bottom 50px of the screen (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video
# walk through in Step 4.

# Detect when the turtle player collides with a car and stop the game if this happens.
# If you get stuck, check the video walk through in Step 5.

# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
# When this happens, return the turtle to the starting position and increase the speed of the cars.
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck,
# check the video walk through in Step 6.

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y_starting_position = randint(-250, 250)
        self.name = self.y_starting_position
        self.goto(320, self.y_starting_position)

    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())




