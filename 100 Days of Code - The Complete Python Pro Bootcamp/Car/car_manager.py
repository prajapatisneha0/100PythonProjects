import turtle
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_IMAGE = "Car.gif"

class CarManager():

    def __init__(self):
        self.all_cars = []
        turtle.register_shape(CAR_IMAGE)
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape(CAR_IMAGE)
            new_car.resizemode("user")
            new_car.turtlesize(stretch_wid=0.01, stretch_len=0.01)
            new_car.color(random.choice(COLORS))
            new_car.up()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

