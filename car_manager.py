from turtle import Turtle
from scoreboard import Scoreboard
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

scoreboard = Scoreboard()
scoreboard.hideturtle()

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        random_no = random.randint(1,6)
        if random_no == 1:
            new_car= Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=320, y=random.randint(-250,250))
            self.cars.append(new_car)

    def move_cars(self): # Move the cars along the x-axis from 320 to -320
       for car in self.cars:
           car.backward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT







