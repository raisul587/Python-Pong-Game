from turtle import  Turtle , Screen
from draw import Draw
screen = Screen()
screen.setup(1080,600)
screen.bgcolor("black")
screen.tracer(0)
draw =Draw()
draw.draw_line()
draw.draw_box()
screen.update()
screen.exitonclick()
