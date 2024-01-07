from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f"score: {self.score}    High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def incresescore(self):
        self.score += 1
        self.clear()
        self.updatescoreboard()

    def restart_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.updatescoreboard()
