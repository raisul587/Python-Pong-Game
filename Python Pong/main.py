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
r_paddle=Paddle((350,0))
l_paddle = Paddle((-350,0))
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
screen.exitonclick()
