from turtle import Turtle
import time
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        global STARTING_POSITIONS
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, cord):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(cord)
        self.snake_body.append(new_segment)

    def move(self):
        time.sleep(0.1)
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[seg_num - 1].xcor()
            y_cor = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def add_snake(self):
        self.add_segment(self.snake_body[-1].pos())

    def reset_snake(self):
        for bod in self.snake_body:
            bod.ht()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def body_collision(self):
        for parts in self.snake_body[1:]:
            if self.head.distance(parts) < 15:
                return True
        return False

