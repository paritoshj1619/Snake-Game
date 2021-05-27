from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen, Turtle
import time


def try_again():
    screen = Screen()
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    start_game()


def start_game():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen = Screen()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.onkey(try_again, "r")
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                scoreboard.again()


class Game:
    def __init__(self):
        start_game()
