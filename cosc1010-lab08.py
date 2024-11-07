# Isabella Cardoso
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to: Ruby Young
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert(num):
    negative = False
    if num[0] == '-':
        negative = True
        num = num.replace('-', '')
    if '.' in num:
        numsplit = num.split('.')
        if len(numsplit) == 2 and numsplit[0].isdigit() and numsplit[1].isdigit():
            if negative:
                return -1*float(num)
            else:
                return float(num)
        else:
            return False
    elif num.isdigit():
        if negative:
            return -1*int(num)
        else:
            return int(num)
    return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list


def slope(m, b, lower_bound, upper_bound):
    """To find the values in the given linear function"""
    y = []
    if type(lower_bound) is int and type(upper_bound) is int and lower_bound <= upper_bound:
        for x in range(lower_bound, upper_bound+1):
            y.append((m*x)+ b)
    else:
        return False
    return y

print("*" * 75)

while True:
    m = input("Enter a number/integer for 'm' to be the slope or enter 'exit' to exit: ")
    if m.lower() == 'exit':
        break

    b = input("Enter a number/integer to be 'b' to be the intercept or enter 'exit' to exit: ")
    if b.lower() == 'exit':
        break

    lower_b = input("Enter the lowest number you want to solve as the lower bound or enter 'exit' to exit: ")
    if lower_b.lower() == 'exit':
        break

    upper_b = input("Enter the highest number you want to solve as the upper bound or enter 'exit' to exit: ")
    if upper_b.lower() == 'exit':
        break

    m = convert(m)
    b = convert(b)
    lower_b = convert(lower_b)
    upper_b = convert (upper_b)

    y = slope(m, b, lower_b, upper_b)
    print(f"All the values from this linear function is {y}")

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def square_root(a, b, c):
    """Square roots the values that need to be"""
    if type(a) is int and type(b) is int and type(c) is int:
        x = (b**2) - (4*a*c)
        if x < 0:
            return False
        else:
            return x**(1/2 * 1/a)
        
def quadratic(a, b, c):
    """To make a quadratic formula for the while loop to use"""
    if type(a) is int and type(b) is int and type(c) is int:
        x = square_root(a, b, c)
        if x == False:
            print("The number that you used created a negative")
            print(x)
            return None
        else:
            y_value_one = (-b-x)/(2*a)
            y_value_two = (-b-x)/(2*a)
        return(y_value_one, y_value_two)
    else:
        return None
    
while True:
    a = input("Enter a number/integer to be 'a', the leading coefficient, or enter 'exit' to exit: ")
    if a.lower() == 'exit':
        break

    b = input("Enter a number/integer to be 'b', the coefficient of 'x', or enter 'exit' to exit: ")
    if b.lower() == 'exit':
        break

    c = input("Enter a number/integer to be 'c', the y-intercept, or enter 'exit' to exit: ")
    if c.lower() == 'exit':
        break

    a = convert(a)
    b = convert(b)
    c = convert(c)

    y_value_one, y_value_two = quadratic(a, b, c)
    print(f"The two values of for the values that you enter are {y_value_one} and {y_value_two}")