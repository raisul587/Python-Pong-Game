from turtle import  Turtle , Screen
from draw import Draw
from paddle import Paddle
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
game_on = True
while game_on:
    screen.update()
screen.exitonclick()
