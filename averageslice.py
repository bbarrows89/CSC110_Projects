# Bryan Barrows
# CSC 110 - Winter 17
# averageslice.py
#    A program to average a set of numbers.
#    Illustrates interactive loop with two accumulators.

def main():
    moredata = "yes"
    sum = 0.0
    count = 0
    # Using string indexing (moredata[0]) allows us to accept 'yeah', 'yes', 'y', etc as yes values.
    while moredata[0] == 'y':
        x = eval(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", sum / count)

main()
