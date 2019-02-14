#---------------------------------------------------#
# Title: FizzBuzz
# Dev:   RLarge
# Date:  1/22/2019
# ChangeLog: (Who, When, What)
# Russell Large, 1/22/2019, Created script
#---------------------------------------------------#

# ------------------ Instructions ----------------- #

# Write a program that iterates the numbers from 1 to 100 inclusive.
# But for multiples of three print "Fizz" instead of the number.
# But for multiples of five print "Fizz" instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.


# ------------------ Data ------------------------- #

equation = list(range(1, 101))

# ------------------ Processing ------------------- #

for x in equation:
    if x % 3 == 0 and x % 5 == 0: # Multiplicity of 3 & 4
        print("FizzBuzz")
    elif x % 3 == 0: # Multiplicity of 3
        print("Fizz")
        #print("Fizz")
    elif x % 5 == 0: # Multiplicity of 4
        print("Buzz")
    else:
        print(x) # All other values

