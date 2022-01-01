#Turtle Graphics Python

import turtle
import random

from turtle import Screen, Turtle, Canvas
from threading import Thread, active_count
from queue import Queue


QUEUE_SIZE = 1

screen = Screen()

screen.bgcolor('black')
color = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'white']
color2 = ['tomato', 'medium orchid', 'light blue', 'Chartreuse', 'Peru', 'Gold']
count = 0
tort = turtle.Turtle()
hare = turtle.Turtle()
deg = 267
deg2 = -89
#deg = input("Give me a Positive Degree " )
#deg2 = input("ive me a Negative Degree " )
#print(deg)
#print(deg2)


for count in range(10):

    for itr in range(720):
        
        #Hare
        hare.speed(0)
        hare.color(color[itr%6])
        #hare.width(itr/100 + 1) 
        hare.pensize(.50) # width of the drawing tool
        #hare._tracer(10,0)


        #Tort
        tort.speed(1)
        tort.color(color2[itr%6])
        #tort.width(itr/100 + 1) 
        tort.pensize(.50) # width of the drawing tool
        tort._tracer(10,25)
        #tort._update()
        

        tort.forward(itr)
        tort.left(deg)
    
        hare.forward(itr)
        hare.left(deg2)
        

    hare.penup()
    hare.goto(0,0)
    hare.pendown()
    hare.reset

    tort.penup()
    tort.goto(0,0)
    tort.pendown()
    tort.reset

    deg = deg + 7
    deg2 = deg2 - 7
    print(deg,deg2) 

     
turtle.getscreen().getcanvas().postscript(file='outputname.ps')



turtle.exitonclick()       # this to exit cleanly