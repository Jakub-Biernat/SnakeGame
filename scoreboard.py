from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-290, 280)


    def show_score(self, score):
        self.clear()
        self.write(f"Score: {score}", move=False, align="left" ,font=('Arial', 8, 'normal'))

