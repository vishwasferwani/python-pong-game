from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_cor =10
        self.y_cor =10


    def move(self):
        newx = self.xcor() + self.x_cor
        newy = self.ycor() + self.y_cor
        self.goto(newx,newy)


    def bounce(self):
        self.y_cor *= -1

    def collide(self):
        self.x_cor *= -1

    def restart(self):
        self.goto(0,0)
        self.collide()



