from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detects collision with the wall
    if (snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290
            or snake.segments[0].ycor() < -290):
        game_is_on = False
        scoreboard.draw_game_over()
    # Detects collision with food
    if snake.segments[0].distance(food.food.xcor(), food.food.ycor()) < 15:
        food.reset()
        scoreboard.update_scoreboard()
        snake.new_tail()
    # Detects collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.draw_game_over()
screen.exitonclick()
