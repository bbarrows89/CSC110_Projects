# Bryan Barrows
# CSC 110 - Winter 17
# triangle.py

# Further exploring in the graphics module, this program makes use of mouse clicks in our window.
# The user clicks three points, which are then used to draw a triangle.
# The user is then told to click anywhere to quit (which closes window and exits program).


from graphics import *

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

main()
