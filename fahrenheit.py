# Bryan Barrows
# CSC 110 - Winter 17
# fahrenheit.py
# The purpose of this program is to convert a user input temperature from celsius to fahrenheit.

def main():
    celsius = eval(input("What is the Celsius temperature?  "))
    fahrenheit = (9/5) * celsius + 32
    print("The temperature is ",fahrenheit," degrees Fahrenheit.")

main()
