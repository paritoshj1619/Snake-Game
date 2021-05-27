import time
from turtle import Turtle, Screen
import game


class Introduction(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -40)
        self.write("Rules: \n\n1. Eat food to increase size of your snake\n2. If head of snake collides with any walls "
                   "you loose\n3. If head of snake collides itself you loose", align="center",
                   font=("Arial", 18, "normal"))
        self.screen = Screen()
        time.sleep(5)
        self.clear()
        game.start_game()
