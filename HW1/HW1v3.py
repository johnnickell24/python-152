"""
Description: A house is drawn by a Turtle complete with windows and doors.
Being able to move from the center makes it much more easier for the Turtle to
draw this house, as now the lines will be centered on the origin.
"""

_author_="John Nickell"

_date_="8/29/14"

import turtle
# setting up turtle so that house is center
myWindow= turtle.Screen()
myTurtle= turtle.Turtle();
myTurtle.color("purple")
myTurtle.pensize(4)
myTurtle.penup()
myTurtle.goto(-225,0)
myTurtle.pendown()
#roof
myTurtle.goto(0,200)
myTurtle.goto(225,0)
myTurtle.goto(-225,0)
#house body
myTurtle.goto(-225,-300)
myTurtle.goto(225,-300)
myTurtle.goto(225,0)
#window 1
myTurtle.penup()
myTurtle.goto(-180,-100)
myTurtle.pendown()
myTurtle.goto(-180,-180)
myTurtle.goto(-100,-180)
myTurtle.goto(-100,-100)
myTurtle.goto(-180,-100)
#window 2
myTurtle.penup()
myTurtle.goto(180,-100)
myTurtle.pendown()
myTurtle.goto(100,-100)
myTurtle.goto(100,-180)
myTurtle.goto(180,-180)
myTurtle.goto(180,-100)
#door
myTurtle.penup()
myTurtle.goto(-50,-100)
myTurtle.pendown()
myTurtle.goto(-50,-300)
myTurtle.goto(50,-300)
myTurtle.goto(50,-100)
myTurtle.goto(-50,-100)















myWindow.exitonclick()
