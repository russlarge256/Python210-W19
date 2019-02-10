#-------------------------------------------------#
# Title: Simple Math
# Dev:   Rlarge
# Date:  Sept 16, 2017
# ChangeLog: (Who, When, What)
#   RLarge, 01/12/2019, Created Script

#-------------------------------------------------#

# ----- Objective ----- #
# Create a function that adds,subtracts, multiplies, and divides two numbers from the user's choosing.
# print results on to a screen

# ----- Processing  ----- #

def simplemath():
    """this function adds,subtracts, multiplies, and divides two numbers from the user's choosing."""

    print("please define two numbers you would like to add, subtract, multiply and divide.\n")

    userinput1 = input("Enter the first number:")
    x = int(userinput1)

    userinput2 = input("Enter the second number:")
    y = int(userinput2)

    # print(str(x + y))
    print(x, "plus", y, "equals " + str(x + y))
    print(x, "minus", y, "equals " + str(x - y))
    print(x, "multiplied by", y, "equals " + str(x * y))
    print(x, "divided by", y, "equals " + str(x / y))

simplemath()