#Multiproccessing Turtle Graphics Python

import turtle
from turtle import Canvas, Screen, Turtle

import random

import queue
from queue import Queue
import threading

from threading import Thread, active_count

def process_queue():
    while not graphics.empty():
        (graphics.get())(1)

    if threading.active_count() > 1:
        turtle.ontimer(process_queue, 1)

def threadTurt():
    for i in range(100):
        print(i, "first")

        graphics.put(hare.circle(-5*i))
        graphics.put(hare.right(i))

        graphics.put(turt.circle(5*i))
        graphics.put(turt.left(i))

      

        print(i, "last")
        

    
#turt._tracer(50, 0) #Full-gas
#hare._tracer(50, 0) #Full-gas

graphics = queue.Queue(100) #a thread-safe data structure

turt = turtle.Turtle('turtle')
turt.color(random.random(), random.random(), random.random())
turt.speed(5)

hare = turtle.Turtle('classic')
hare.color = (random.random(), random.random(), random.random())
hare.speed(5)

thread1 = threading.Thread(target=threadTurt)
thread1.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread1.start()

thread2 = threading.Thread(target=threadTurt)
thread2.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread2.start()


turtle.exitonclick()       # this to exit cleanly