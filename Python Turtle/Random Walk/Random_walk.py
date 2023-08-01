import turtle as my_turtle
import random
t=my_turtle.Turtle()
my_turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
    
directions=[0,90,180,270]
t.pensize(15)
t.speed("fastest")
for i in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))
    