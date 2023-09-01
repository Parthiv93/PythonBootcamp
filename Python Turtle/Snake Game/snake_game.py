from turtle import Turtle, Screen
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
starting_positions=[(0,0),(-20,0),(-40,0)]
segments=[]

for positions in starting_positions:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions)
    segments.append(new_segment)
    
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(segments)-1,0,-1):
        new_x=segments[i-1].xcor()
        new_y=segments[i-1].ycor()
        segments[i].goto(new_x,new_y)
    segments[0].forward(20)


screen.exitonclick()