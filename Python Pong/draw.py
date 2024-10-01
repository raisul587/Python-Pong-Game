from turtle import  Turtle
class Draw(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.pencolor("white")
        self.penup()
        self.goto(0,300)
        self.right(90)
        self.pensize(4)
        self.ht()
    def draw_line(self):
        for _ in range(40):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
    def draw_box(self):
        self.pensize(10)
        self.goto(-100,200)
        self.pendown()
        for _ in range(4):
            self.forward(20)
            self.right(90)
            self.forward(70)
        self.penup()
        self.goto(100,270)
        self.pendown()
        self.pensize(10)
        self.forward(70)
        
