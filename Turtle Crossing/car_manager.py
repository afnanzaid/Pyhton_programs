from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.all_cars_left = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car_right(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 0)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars_right(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car_left(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(0, 250)
            new_car.goto(-300, random_y)
            self.all_cars_left.append(new_car)

    def move_cars_left(self):
        for car in self.all_cars_left:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
