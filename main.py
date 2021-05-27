from turtle import Screen
from introduction import Introduction

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

introduction = Introduction()

screen.exitonclick()
