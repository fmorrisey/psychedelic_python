#Turtle Graphics Python

import turtle
import queue
from turtle import Screen, Turtle
from threading import Thread, active_count
from queue import Queue

screen = Screen()
screen.bgcolor('black')

tort = turtle.Turtle()
tort.showturtle()
#tort.speed(0)
hare = turtle.Turtle()
hare.showturtle()
#hare.speed(0)

count = 360

QUEUE_SIZE = 10

def process_queue():
    while not actions.empty():
        action, *arguments = actions.get()
        action(*arguments)

    if active_count() > 100:
        screen.ontimer(process_queue, 100)

actions = Queue(QUEUE_SIZE)  # a thread-safe data structure

def move(turtle):
    for itr in range(count):
        actions.put((hare.forward, itr))
        actions.put((hare.left, 89))
        actions.put((tort.forward, itr))
        actions.put((tort.left, -89))

def color(turtle):
    color = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'white']
    color2 = ['tomato', 'medium orchid', 'light blue', 'Chartreuse', 'Peru', 'Gold']
    for itr in range(count):
        hare.color(color[itr%6])
        tort.color(color[itr%6])


Thread(target=move, args=[hare], daemon=True).start()
Thread(target=move, args=[tort], daemon=True).start()

process_queue()
color(hare)
move(hare)
color(tort)
move(tort)

turtle.exitonclick()       # this to exit cleanly