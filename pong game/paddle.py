import turtle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(xcor,ycor)


    def upward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def downward(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)






