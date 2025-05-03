from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.penup()
        self.color("white")
        self.goto(x=0, y=265)
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "bold"))


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "bold"))

    def get_high_score(self):
        with open("data.txt", "r") as file:
            return int(file.read())

    def update_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.score))




    def add_score(self):
        self.score += 1
        self.update_score()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_score()

