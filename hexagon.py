from turtle import  Turtle, Screen

hexagons_count = 0

my_turtle = turtle.Turtle()       # x is not a good name for a Turtle object
# my_turtle.speed(.25)            # see @cdlane comment reported in a note under.

def draw_hexagon():               # use explicit names respecting python conventions (no camel case)
    global hexagons_count         # need global to modify the variable in the function scope
    for idx in range(24):         # use different dummy variable names in your loops 
        for jdx in range(6):      # use different dummy variable names in your loops
            my_turtle.forward(100)
            my_turtle.left(60)
        hexagons_count += 1
        my_turtle.left(15)
        print(hexagons_count)

draw_hexagon()             # need parenthesis to call the function

turtle.exitonclick()       # this to exit cleanly