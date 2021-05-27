from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\n\nFinal Score: {self.score}", align="center", font=("Arial", 20, "bold"))
        self.goto(0, -30)
        self.write(f"Press 'r' to Retry", align="center", font=("Arial", 13, "normal"))

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()