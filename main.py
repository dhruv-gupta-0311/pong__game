from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
score = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #bounce the ball when hit to left or right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    #paddle miss right and reset score
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # paddle miss left  and reset score
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.l_score == 5 or score.r_score == 5:
        score.end()
        break

    ball.move()
    screen.update()

screen.exitonclick()






