from turtle import Turtle
ALIGNMENT="center"
FONT="ARIAL"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.highscore=self.readscore()
        self.score= 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score is: {self.score}, High score:{self.highscore}",align="center",font=("Arial", 24, "normal"))

    def reset(self):
        if self.score> self.highscore:
            self.highscore= self.score
        self.score = 0
        self.update_scoreboard()
        self.writescore()

    def increase(self):
        self.score+=1
        self.update_scoreboard()

    def readscore(self):
        with open("data.txt","r") as file:
            highscore=file.read()
        return int(highscore)

    def writescore(self):
        with open("data.txt","w") as file:
            file.write(str(self.highscore))
