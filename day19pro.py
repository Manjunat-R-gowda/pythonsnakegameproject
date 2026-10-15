from turtle import Screen
from food import Food
import time
from scoreboard import Score
from snake import Snake

screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("------Snake game--------")
screen.tracer(0)




'''start=[(0,0),(-20,0),(-40,0)]
segments=[]
for position in start:
    new_pro=Turtle("square")
    new_pro.color("white")
    new_pro.penup()
    new_pro.goto(position)
    segments.append(new_pro)'''



'''new_proo=Turtle("square")
new_proo.color("white")
new_proo.goto(-20,0)


new_prooo=Turtle("square")
new_prooo.color("white")
new_prooo.goto(-40,0)
segments.append(new_pro)
segments.append(new_proo)
segments.append(new_prooo)'''

scree=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(scree.up,"Up")
screen.onkey(scree.down,"Down")
screen.onkey(scree.left,"Left")
screen.onkey(scree.right,"Right")




is_on=True
while is_on:
    screen.update()
    time.sleep(0.1)
    scree.move()

    if scree.head.distance(food)<15:
        food.refresh()
        scree.extended()
        score.increase()

    if scree.head.xcor()>280 or scree.head.xcor()<-280 or scree.head.ycor()>280 or scree.head.ycor()<-280:
        is_on=False
        score.goto(0,0)
        score.write("GAME OVER",align="center",font=("arial",20,"normal" ))


    for segments in scree.segments:
        if segments==scree.head:
            pass
        elif scree.head.distance(segments)<10:
            is_on=False
            score.goto(0,0)
            score.write("GAME OVER",align="center",font=("arial",20,"normal" ))


        

    
    '''for segm in range(len(segments)-1,0,-1):
        new_x=segments[segm-1].xcor()
        new_y=segments[segm-1].ycor()
        segments[segm].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)'''


































screen.exitonclick()