from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
screeny = Screen()
screeny.setup(width=600, height=600)
screeny.bgcolor("black")
screeny.title("!Welcome to Snake Game!")
screeny.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screeny.listen()
screeny.onkey(snake.up, "Up")
screeny.onkey(snake.down, "Down")
screeny.onkey(snake.left, "Left")
screeny.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screeny.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.incresescore()
        snake.extend()
    if snake.head.xcor() > 299 or snake.head.xcor() < -300 or snake.head.ycor() > 299 or snake.head.ycor() < -300:
        score.restart_score()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.restart_score()
            snake.reset()

screeny.exitonclick()
