# Bryan Barrows
# CSC 110 - Winter 17
# click.py


from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(5):
        p = win.getMouse()
        print("You clicked at: (", p.getX(), ",",p.getY(),")")

main()
