from turtle import Turtle
ALIGNMENT = "left"
FONT = ('Arial', 10, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-290, 275)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=ALIGNMENT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write_score()

