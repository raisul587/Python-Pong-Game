from turtle import  Turtle , Screen
from draw import Draw
from paddle import Paddle
from ball import  Ball
import time
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("The Famous Pong Arcade Game")
screen.tracer(0)
draw =Draw()
draw.draw_line()
draw.draw_box()
r_paddle=Paddle((370,0))
l_paddle = Paddle((-370,0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")
screen.listen()
ball = Ball((0,0))
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_x()
    #see if paddle miss the ball
    if ball.xcor()>350 or ball.xcor()<-350:
        ball.goto(0,0)
        ball.bounce_x()
screen.exitonclick()
