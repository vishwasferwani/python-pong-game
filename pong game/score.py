from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(f"{self.score}", align="center", font=("arial", 40, "normal"))


    def increase_Score(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}", align="center", font=("arial", 40, "normal"))

