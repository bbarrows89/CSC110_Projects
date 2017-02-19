# Bryan Barrows
# CSC 110 - Winter 17
# Week 7 Practice Exercise
# filename:  surfacearea.py
# This function takes base length, width, and height of a pyramid and prints the pyramid's surface area.

from math import *

def main():
    length = eval(input("Enter the base length of the pyramid: ")) # user prompted for base length
    width = eval(input("Enter the base width of the pyramid: ")) # user prompted for base width
    height = eval(input("Enter the height of the pyramid: ")) # user prompted for pyramid height

    surface_area = ((length * width) + length * sqrt((width/2)**2 +height**2) + width * sqrt((length/2)**2 + height**2))

    print("The surface area of the pyramid is approximately: ", (round(surface_area, 2)))

main()
