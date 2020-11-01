###    Write a program that calculates the cost per square inch of a circular pizza,given its diameter and price.
import math

def f():
    print ("The following program will calulate the per square inch price of pizza")
    user_input_diameter = float(input("Enter diameter of pizza [in inches]: "))
    user_input_price = float(input("Enter price of pizza [in dollars]: "))
    if (user_input_diameter > 0 and user_input_price > 0):
        area_pizza = (math.pi) * (user_input_diameter ** 2) * 0.25
        cost_per_square_inch = user_input_price/area_pizza
        print ("The price per square inch of the given pizza is: ", cost_per_square_inch, " $/square inch")
        f()
    else:
        print ("Mr.Smartypants trynna check my code huh? Well guess what, its not gonna loop for you. Now you have to enter the function manually again. Don't get angry, you deserve it.")
