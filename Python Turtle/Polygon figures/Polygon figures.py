import turtle as my_turtle
import random
t=my_turtle.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def my_shapes(no_of_sides):
    angle=360/no_of_sides
    for i in range(no_of_sides):
        t.forward(100)
        t.right(angle)
 
for i in range(3,11):
    t.color(random.choice(colours))
    my_shapes(i)

    