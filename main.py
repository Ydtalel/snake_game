from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

snake = Snake()
food = Food()
score = Score()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")

screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

go_on = True


while go_on:
    screen.update()
    time.sleep(0.1)
    score.show_score()
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()


    # detect collision with tail.
    reverse_segments_except_first = snake.segments[1:]
    for segment in reverse_segments_except_first:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()