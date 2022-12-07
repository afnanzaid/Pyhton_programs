import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.score()
    cars.create_car_right()
    cars.move_cars_right()
    cars.create_car_left()
    cars.move_cars_left()


    # Detect collision with wall
    if player.ycor() > 280:
        player.reset_move()
        scoreboard.increase_level()
        cars.increase_speed()

    # Detect collision with right_car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with left_car
        for car in cars.all_cars_left:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
