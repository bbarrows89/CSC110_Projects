# Bryan Barrows
# CSC 110 - Winter 17
# Week 8 Practice Exercise - A
# filename:  pyramidVolume.py
# This function takes base length, width, and height of a pyramid and prints the pyramid's volume.


from math import *

def main():
    length = eval(input("Enter the base length of the pyramid: ")) # user prompted for base length
    width = eval(input("Enter the base width of the pyramid: ")) # user prompted for base width
    height = eval(input("Enter the height of the pyramid: ")) # user prompted for pyramid height

    volume = (length * width * height) / 3

    print("The volume of the pyramid is approximately: ", (round(volume, 2)), " cubic units.")

    # the output is simply in cubic units... this allows user to input whatever type of unit they'd like...
    # including metric, feet, etc... however, the tradeoff is that our output is somewhat vague as a result.
    # In the future, it would be good to add commas that separate the thousands place for large outputs.
    

main()
