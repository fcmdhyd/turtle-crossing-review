from turtle import Turtle

STARTING_POSITION = (0, -180)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 180


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
