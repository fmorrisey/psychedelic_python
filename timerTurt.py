from turtle import Screen, Turtle
from threading import Thread, active_count
from queue import Queue


screen = Screen()


a = Turtle('square', visible=True)
a.speed(0)
a.color('red')
a.penup()
a.setx(-300)
a.setheading(0)
a.pendown()
a.showturtle()

b = Turtle('circle', visible=False)
b.speed(0)
b.color('green')
b.penup()
b.setx(300)
b.setheading(180)
b.pendown()
b.showturtle()

### Subsequent variations start here ###


### Subsequent variations end here ###
QUEUE_SIZE = 1

def process_queue():
    while not actions.empty():
        action, *arguments = actions.get()
        action(*arguments)

    if active_count() > 1:
        screen.ontimer(process_queue, 100)

actions = Queue(QUEUE_SIZE)  # a thread-safe data structure

def move(turtle):
    while turtle.distance(0, 0) > 1:
        actions.put((turtle.forward, 1))

Thread(target=move, args=[a], daemon=True).start()
Thread(target=move, args=[b], daemon=True).start()

process_queue()

move(a)
move(b)
screen.mainloop()