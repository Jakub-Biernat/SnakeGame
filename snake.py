from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.setup_snake()

    def setup_snake(self):
        for num_of_snake in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            starting_position = STARTING_POSITIONS[num_of_snake]
            new_segment.goto(starting_position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_seg_num = seg_num - 1
            next_position = self.segments[next_seg_num].position()
            self.segments[seg_num].goto(next_position)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)
