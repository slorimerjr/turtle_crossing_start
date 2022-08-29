import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
#
# 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
#
# 3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []
car_index = 0

screen.listen()

screen.onkey(player.up, "Up")

game_increments = 0
game_is_on = True
while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    scoreboard.update_scoreboard()
    game_increments += 1

    # checks game_increments to determine if a new car should be made (new car made every 6th time the game loop runs).
    if game_increments % 6 == 0:
        car = CarManager()
        cars.append(car)
        car_index += 1

    # ensures that all cars will continuously move across the screen
    for all_cars in cars:
        all_cars.move()
        if player.distance(all_cars) < 25:
            game_is_on = False
            scoreboard.game_over()
            player.move_speed = 0.1

    # increases score, resets turtle position, increases car speed
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.score += 1



screen.exitonclick()