#Turtle Graphics Python

import turtle
from itertools import count
win = turtle.Screen()
win.bgcolor('black')
color = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
count = 59
count2 = 73
tort = turtle.Turtle()


for itr in range(360):
    tort.speed(10)
    tort.color(color[itr%6])
    tort.forward(itr)
    tort.width(itr/100 + 1) 
    tort.pensize(3) # width of the drawing tool
    tort.left(count)
    count = count + 1.0035
    print(count)
      
for itr in range(360):
    tort.speed(5)
    tort.color(color[itr%6])
    tort.forward(itr)
    tort.width(itr/50 + 1) 
    tort.pensize(3) # width of the drawing tool
    tort.left(count2)
    count2 = count2 + 1.0087
    print(count)
   


turtle.exitonclick()       # this to exit cleanly