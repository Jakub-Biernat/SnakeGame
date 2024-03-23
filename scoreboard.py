from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-290, 280)

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="left", font=('Arial', 8, 'normal'))

    def add_score(self):
        self.score += 1

