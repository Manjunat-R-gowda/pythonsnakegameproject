from turtle import Turtle,Screen

START_FORMATE=[(0,0),(-20,0),(-40,0)]
MAKE= 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    
    def __init__(self):
        self.segments=[]
        self.create()
        
        self.head=self.segments[0]

    def create(self):
        
        
        for position in START_FORMATE:
            self.addsegment(position)


    def move(self):   
        for segm in range(len(self.segments)-1,0,-1):
            new_x=self.segments[segm-1].xcor()
            new_y=self.segments[segm-1].ycor()
            self.segments[segm].goto(new_x,new_y)
        self.head.forward(MAKE)

    def extended(self):
        self.addsegment(self.segments[-1].position())



    def addsegment(self,position):
            new_pro=Turtle("square")
            new_pro.color("white")
            new_pro.penup()
            new_pro.goto(position)
            self.segments.append(new_pro)


    def up (self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

        
            

