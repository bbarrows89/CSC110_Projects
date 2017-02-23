# Bryan Barrows
# CSC 110 - Winter '17
# BMI Calculator
# Week 8 Practice Exercise - B
# bmi_calc.py

# Building on the chapter material covering Decision Structures, we were asked
# to build a Python program that asks user for height & weight, then calculates
# their BMI. Finally, a decision structure is used to inform user of which
# "weight class" they fall into based upon their BMI score.


def main():
    print("Let's calculate your BMI! First, we'll start with your height...")
    try:
        height_ft = eval(input("How many feet tall are you?  "))
        height_in = eval(input("And how many inches?  "))
        weight = eval(input("And, finally, how many pounds do you weigh?  "))

        height = (height_ft * 12) + height_in

        bmi = round((weight / (height * height) * 703),2)
        
    

        if bmi < 18.5:
            print("Your BMI is", bmi, "which means you are underweight.")

        elif bmi < 25:
            print("Your BMI is", bmi, "which means you are normal weight.")

        elif bmi < 30:
            print("Your BMI is", bmi, "which means you are overweight.")

        else:
            print("Your BMI is", bmi, "which means you are very overweight.")

    except ZeroDivisionError:
        print("Height must be greater than zero.")

    except NameError:
        print("Please use numerical values.")
        
    

main()
