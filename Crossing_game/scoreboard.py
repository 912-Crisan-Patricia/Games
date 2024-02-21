from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-180,260)
        self.level=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score is :{self.level}",align="center",font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game over",align="center",font=FONT)

    def increaselvl(self):
        self.level+=1
        self.update_score()

