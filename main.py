from turtle import Turtle, Screen
from snake import Snake
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Ssssnake Game")
my_screen.tracer(0)


snake = Snake()
while True:
    my_screen.update()
    time.sleep(0.1)
    snake.move()









my_screen.exitonclick()