from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move_cars()
    scoreboard.show_score()

    # detect collision by car
    for car in car_manager.cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.finish()

    # Check if turtle reached other side
    if player.ycor() >300:
        player.player_reset()
        car_manager.inc_speed()
        scoreboard.inc_level()

screen.exitonclick()