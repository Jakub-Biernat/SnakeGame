from turtle import Turtle, Screen
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Ssssnake Game")
my_screen.tracer(0)



segments = []


def setup_snake():
    for num_of_snake in range(3):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=num_of_snake * -20, y=0)
        segments.append(new_segment)
    #my_screen.update()

setup_snake()

is_running = True
while is_running:
    my_screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        next_seg_num = seg_num - 1
        next_position = segments[next_seg_num].position()
        segments[seg_num].goto(next_position)
    segments[0].forward(20)









my_screen.exitonclick()