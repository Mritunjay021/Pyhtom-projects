from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_s = 0
        self.r_s = 0
        updatescore()

        def updatescore(self):
            self.clear()
            self.goto(-100, 280)
            self.write(self.l_s, align="center", font=("Courier,", 80, "normal"))
            self.goto(100, 280)
            self.write(self.r_s, align="center", font=("Courier,", 80, "normal"))

        def l_point(self):
            self.l_score += 1
            self.updatescore()

        def r_point(self):
            self.r_score += 1
            self.updatescore()


