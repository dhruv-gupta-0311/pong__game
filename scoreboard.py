from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Ariel", 30, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Ariel", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def end(self):
        if self.l_score == 5:
            self.goto(0, 0)
            self.write("l won", align="center", font=("Ariel", 30, "normal"))

        elif self.r_score == 5:
            self.goto(0, 0)
            self.write("r won", align="center", font=("Ariel", 30, "normal"))
