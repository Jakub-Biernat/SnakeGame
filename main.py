from turtle import Screen
from snake import Snake
from food import Food
import time
GAME_SPEED = 0.05

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Ssssnake Game")
my_screen.tracer(0)


snake = Snake()
food = Food()

my_screen.listen()
my_screen.onkey(snake.up, "w")
my_screen.onkey(snake.down, "s")
my_screen.onkey(snake.left, "a")
my_screen.onkey(snake.right, "d")


while True:
    my_screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()









my_screen.exitonclick()