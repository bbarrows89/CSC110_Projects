# Bryan Barrows
# Week 4 Practice Exercise
# CSC 110 - 9830
# Jan 29th, 2017
# bryangraphic.py
# Specs for this project: must include a polygon, a shape besides polygon, a text caption, and some colors.

from graphics import *

def main():

    win = GraphWin('Bryan Barrows', 420, 420)
    win.setBackground("blue")
    goHawks = Text(Point(210,385), "Go Hawks!")
    goHawks.setTextColor("green")
    goHawks.setSize(18)
    goHawks.draw(win)
    one = Rectangle(Point(75, 30), Point(140, 350))
    one.setFill("green")
    one.draw(win)
    twoTop = Rectangle(Point(220, 30), Point(370, 75))
    twoTop.setFill("green")
    twoTop.draw(win)
    twoBottom = twoTop.clone()
    twoBottom.draw(win)
    twoBottom.move(0, 275)
    twoMiddle = twoBottom.clone()
    twoMiddle.draw(win)
    twoMiddle.move(0, -137.5)
    twoRS = Polygon(Point(330, 75), Point(330, 170), Point(370, 170), Point(370, 75))
    twoRS.setFill("green")
    twoRS.draw(win)
    twoLS = twoRS.clone()
    twoLS.draw(win)
    twoLS.move(-110, 137.5)



main()
