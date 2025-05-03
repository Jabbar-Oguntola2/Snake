from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)

    def refresh(self):
        self.ht()
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)
        self.showturtle()







