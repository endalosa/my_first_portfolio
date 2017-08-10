from turtle import *
import math

# Name your Turtle.
t = Turtle()


# Set Up your screen and starting position.
t.penup()
setup(850,850)
bgcolor("black")

t.penup()
t.setx(200)
t.sety(200)


sides = input('How many sides?: ')
sides= int(sides)
angle = 360 / sides
color = input('What color?: ')
scale = input('Big, medium or small? Type B for big, M for medium, S for small: ')
if scale == 'B':
    length = 300
elif scale == 'M':
    length = 200
elif scale == 'S':
    length = 100


#define draw shape
def drawshape(sides, color):
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for sides in range(sides):
        t.forward(length)
        t.right(angle)
    t.end_fill()

#move!
drawshape(sides, color)

# Close window on click.
exitonclick()
