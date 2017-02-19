# Bryan Barrows
# CSC 110 - Winter 17
# HW 2 - Problem 3 (geometric series 1/2 + 1/4 + 1/8, ....)

# This function approx(x) expects a value for x which tells us how many
# terms of the geometric sequence we'd like to add.
# For example, approx(3) should = 0.875.

# HW 2, question 3, part a

def approx(x):
    approx = 0
    current = 1
    for n in range(x):
        current = current / 2
        approx = approx + current
    diff = round(1 - approx, 3)
    print("This is the approximation of the first three terms of the geometric sequence.")
    print(approx)
    print("This is the difference between the value of the geometric series (1) and our approximation.")
    print(diff)

numTerms = eval(input("Enter number of terms: ")) # user is prompted for number of terms to calculate
approx(numTerms)

# HW 2, question 3, part b

def approx2(x):
    approx = 0
    current = 1
    print("This shows how close our approximation gets to 1 as the number of terms increase.")
    for n in range(x):
        current = current / 2
        approx = approx + current
        diff = round(1 - approx, 3)
        print(approx)

approx2(3) #in this case, we just feed our approx2 funtion an input of 3.
    


## HW 2, question 3, part c:

## def approx2(x):
##    approx = 0
##    current = 1
##    print("This shows how close our approximation gets to 1 as the number of terms increase.")
##        for n in range(x):
##            current = current / 2
##            approx = round(approx + current, 2)
##            print(approx)
##
##  approx2(6)
##
## When our approx values are rounded to two decimal places, we need 6 or more terms
##  in order to get an approximate value of 0.99 or greater.

