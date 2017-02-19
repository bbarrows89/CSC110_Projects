# Bryan Barrows
# CSC 110 - Winter 17
# suess.py

# As I was exploring the chapter on graphics, there was an excellent example of "Red Fish, Blue Fish",
# which I took the liberty of playing with and exploring.

# I found it really cool how by definining so many variables within our drawFish method, it is possible
# to simply call the drawFish method with a number of parameters.
# A fun, simple demonstration on the power of modularity.

from graphics import *

def main():

    win = GraphWin('Seuss')
    drawFish(win, 25, 25, 85, 55, label="One Fish")
    drawFish(win, 35, 110, 75, 140)
    drawFish(win, 50, 150, 75, 170, label="Two Fish" )
    drawFish(win, 145, 35, 170, 55, 'red', "Red Fish" )
    drawFish(win, 125, 110, 175, 145, 'blue', "Blue Fish")

def drawFish(win,p1x, p1y, p2x, p2y,color=None, label=None):
    p1 = Point(p1x, p1y)
    p2 = Point(p2x, p2y)
    fish = Oval(p1,p2)
    diffX = p2x-p1x
    diffY = p2y-p1y
    fishEye = Point((p1x + diffX/6),(p1y +(diffY/2) - diffY/6))
    fishTail = Polygon(Point(p2x, p1y+diffY/2), Point(p2x+diffX/6, p1y), Point(p2x+diffX/6, p1y+diffY))
    fish.setFill(color)
    fishTail.setFill(color)
    caption = Text(Point(p1x + 20, p1y + diffY + 10), label)
    fish.draw(win)
    fishEye.draw(win)
    fishTail.draw(win)
    caption.draw(win)

main()
