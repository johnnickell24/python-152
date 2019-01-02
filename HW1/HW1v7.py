"""
Description: A house is drawn by a Turtle complete with windows, a chimney,
and doors. Being able to move to the center makes it much more easier for
the Turtle to draw this house, as now the lines will be centered on the origin.
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
myTurtle.color("#FF0000")
myTurtle.begin_fill()
myTurtle.goto(0,200)
myTurtle.goto(225,0)
myTurtle.goto(-225,0)
myTurtle.end_fill()

#house body
myTurtle.color("#1A0CE8")
myTurtle.begin_fill()
myTurtle.goto(-225,-300)
myTurtle.goto(225,-300)
myTurtle.goto(225,0)
myTurtle.end_fill()

#window 1
myTurtle.color("#0DFF9F")
myTurtle.begin_fill()
myTurtle.penup()
myTurtle.goto(-180,-100)
myTurtle.pendown()
myTurtle.goto(-180,-180)
myTurtle.goto(-100,-180)
myTurtle.goto(-100,-100)
myTurtle.goto(-180,-100)
myTurtle.end_fill()

#window 2
myTurtle.begin_fill()
myTurtle.penup()
myTurtle.goto(180,-100)
myTurtle.pendown()
myTurtle.goto(100,-100)
myTurtle.goto(100,-180)
myTurtle.goto(180,-180)
myTurtle.goto(180,-100)
myTurtle.end_fill()

#door
myTurtle.color("#0CFF00")
myTurtle.begin_fill()
myTurtle.penup()
myTurtle.goto(-50,-100)
myTurtle.pendown()
myTurtle.pensize(6)
myTurtle.goto(-50,-300)
myTurtle.goto(50,-300)
myTurtle.goto(50,-100)
myTurtle.goto(-50,-100)
myTurtle.end_fill()

#chimney
myTurtle.penup()
myTurtle.goto(100,115)
myTurtle.color("#A74AC7")
myTurtle.begin_fill()
myTurtle.pendown()
myTurtle.right(270)
myTurtle.forward(100)
myTurtle.right(90)
myTurtle.forward(20)
myTurtle.right(90)
myTurtle.forward(120)
myTurtle.goto(100,115)
myTurtle.end_fill()

#Attic Circle Window
myTurtle.penup()
myTurtle.goto(-25,80)
myTurtle.color("gold")
myTurtle.pendown()
myTurtle.begin_fill()
myTurtle.circle(25)
myTurtle.end_fill()
ht()
myWindow.exitonclick()
