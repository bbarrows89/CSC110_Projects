# Bryan Barrows
# Week 11 Practice Exercises
# CSC 110 - Winter 17
# whattriange.py
# This function asks user for the length of each side of a triangle.
# It then outputs a string indicating what kind of triangle the user input.



def main():

    s1 = eval(input("Please enter the length of Side 1: "))
    s2 = eval(input("Please enter the length of Side 2: "))
    s3 = eval(input("Please enter the length of Side 3: "))

    if s1 == s2 == s3:
        print("Equilateral Triangle")

    elif s1 != s2 != s3:
        print("Scalene Triangle")

    else:
        print("Isosceles Triangle")

main()
