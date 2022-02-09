from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.show_score()

    def show_score(self):
        self.hideturtle()
        self.penup()
        self.goto(-225, 255)
        self.write(arg=f" Level:{self.level} ", align=ALIGN, font=FONT)
        self.clear()

    def inc_level(self):
        self.level += 1

    def finish(self):
        self.penup()
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)



