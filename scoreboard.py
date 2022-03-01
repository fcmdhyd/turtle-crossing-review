from turtle import Turtle

FONT = ("Courier", 32, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.goto(0,0)
        self.write("[GAME OVER]", align="center", font=FONT)