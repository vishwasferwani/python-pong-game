import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time


screen = Screen()
screen.title("Pong")
screen.listen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)


own_paddle= Paddle(340,0)
opponent_paddle= Paddle(-340,0)
ball =Ball()
right_score =Scoreboard(70,230)
left_score =Scoreboard(-70,230)

is_game_on = True


while is_game_on:
    sleep = 0.1
    time.sleep(sleep)
    screen.update()
    ball.move()
    screen.onkeypress(key="Up", fun=own_paddle.upward)
    screen.onkeypress(key="Down",fun=own_paddle.downward)
    screen.onkeypress(key="w",fun=opponent_paddle.upward)
    screen.onkeypress(key="s",fun=opponent_paddle.downward)

    x = ball.xcor()
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce()


    if ball.distance(own_paddle) < 40 and ball.xcor() > 320 or ball.distance(opponent_paddle) <40 and ball.xcor() < -320:
        ball.collide()
        sleep -= 0.09
        time.sleep(sleep)

    #right paddle miss
    if ball.xcor() > 390:
        time.sleep(0.4)
        ball.restart()
        own_paddle.reset()
        opponent_paddle.reset()
        own_paddle = Paddle(340, 0)
        opponent_paddle = Paddle(-340, 0)
        left_score.increase_Score()

    #left paddle miss
    if ball.xcor() < -390:
        time.sleep(0.4)
        ball.restart()
        ball.move()
        own_paddle.reset()
        opponent_paddle.reset()
        own_paddle = Paddle(340, 0)
        opponent_paddle = Paddle(-340, 0)
        right_score.increase_Score()

screen.exitonclick()