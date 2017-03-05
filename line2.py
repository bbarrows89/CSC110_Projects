# Bryan Barrows
# CSC 110 - Winter 17
# HW 3 - Problem 2b
# line2.py

# This program allows the user to draw a line segment and then displays some graphical
# and textual information about the line segment.

# This program adds a label to the window indicating what the midpoint of the line is.

from graphics import *
from math import *

def main():

    # Introduction
    
    print("This program allows you to draw a line and learn information about it.")
    print("Click any two points to begin!")

    # Draw the window, includes another text prompt for user (just in case :)
    
    win = GraphWin("Line Segment Information", 500, 500)
    win.setCoords(0.0, 0.0, 50.0, 50.0)
    message = Text(Point(25.0, 1), "Click the two endpoints of your line to begin")
    message.setSize(18)
    message.draw(win)

    # Get mouse clicks to determine endpoints and draw the line.

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    theLine = Line(p1, p2)
    theLine.draw(win)

    # Draw the midpoint in cyan AND add a label.

    midPoint = theLine.getCenter()
    midPoint.setFill("cyan")
    midPoint.draw(win)
    labelX = round(midPoint.getX(),2)
    labelY = round(midPoint.getY(),2)
    midLabel = Text(Point(labelX + 4, labelY + 4), "Your midpoint is approximately: "+ str(labelX) + ", "  + str(labelY) + ".")
    midLabel.draw(win)

    # Calculate and print the length and slope of line
    try:
    
        x1 = p1.getX()
        x2 = p2.getX()
        y1 = p1.getY()
        y2 = p2.getY()
        dx = x2 - x1
        dy = y2 - y1
        slope = dy/dx
        length = sqrt((dx)**2+(dy)**2)
        print("The slope of this line is: ", slope)
        print("The length of this line is: ", length)

    except ZeroDivisionError:
        print("You mouse clicks cannot be in the same place.")

    # wait for another click to exit
    
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()


main()
