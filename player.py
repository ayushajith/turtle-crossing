from turtle import Turtle, Screen


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        screen.tracer(0)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        screen.update()
        self.left(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def player_reset(self):
        self.goto(STARTING_POSITION)
        screen.update()


