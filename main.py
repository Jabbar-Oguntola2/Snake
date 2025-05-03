from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
screen.listen()
score = Scoreboard()
food = Food()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.add_snake()
        score.add_score()

    if (snake.head.xcor() > 289 or snake.head.xcor() < -289) or snake.head.ycor() > 289 or snake.head.ycor() < -289:
        score.reset()
        snake.reset_snake()

    if snake.body_collision():
        score.reset()
        snake.reset_snake()





screen.exitonclick()