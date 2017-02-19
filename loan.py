# Bryan Barrows
# CSC 110 - 9830
# File: loan.py
# This script prompts user for inputs and calculates monthly payments.

def main():
    print("Let's calculate your monthly payment! ")
    L = eval(input("What is your total loan amount? "))
    rate = eval(input("What is your monthly interest rate (as a decimal)? "))
    N = eval(input("Over how many months will you be paying this loan off? "))

    payments = L * (rate * (1 + rate)**N) / ((1 + rate)**N -1)  

    print ("Your monthly payments are: $", round(payments, 2))
           
main()
    
