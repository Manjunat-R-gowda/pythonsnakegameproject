from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        
        self.hideturtle()
        self.updated()

    def updated(self):
        self.write(f"score={self.score}",align="center",font=("arial",20,"normal" ))


    def increase(self):
        self.score+=1
        self.clear()
        self.updated()
        



