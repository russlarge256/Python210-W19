# -------------------------- #
# Title: GridPrinter
# Changelog:
# Russell Large, 1-22-19
# -------------------------- #

# ----------- Layout -------- #
# Data = parameters used
# Phase 1 (non-function, static script)
# Phase 2 (function, one parameter)
# Phase 3 (function, two parameters)


#-------------- Phase 1 ----------- #


# ------------ Data ----------#

PlusSign = '+ '
MinusSign = ' - '
ColumnSign = '| '
space = ' '
MiddleColumn = (ColumnSign + space*12 + ColumnSign + space*12 + ColumnSign)


Line1Type = (PlusSign + (MinusSign*4) + PlusSign + (MinusSign*4) + PlusSign) # Long
Line2Type = (((ColumnSign + space*12 + ColumnSign + space*12 + ColumnSign) + '\n')*4) # Long
Line3Type = (MiddleColumn + '\n')*3 + MiddleColumn

print(Line1Type)
print(Line2Type, end='')  # lat
print(Line1Type)
print(Line2Type, end='')  # lat
print(Line1Type)

#-------------- Phase 2 ----------- #

def GridPrinter(x):

    PlusSign = '+ '
    MinusSign = ' - '
    ColumnSign = '| '
    space = ' '
    MiddleColumn = (ColumnSign + space * 12 + ColumnSign + space * 12 + ColumnSign)

    Line1Type = (PlusSign + (MinusSign * 4*x) + PlusSign + (MinusSign * 4*x) + PlusSign)  # Long
    Line2Type = (((ColumnSign + space * 12*x + ColumnSign + space * 12*x + ColumnSign) + '\n') * 4)  # Long
    Line3Type = (MiddleColumn + '\n') * 3 + MiddleColumn

    print(Line1Type)
    print(Line2Type*x, end='')  # lat
    print(Line1Type)
    print(Line2Type*x, end='')  # lat
    print(Line1Type)


GridPrinter(1)

# ------------ Phase 3 ------------- #

def GridPrinter2(x,y):

    PlusSign = '+ '
    MinusSign = ' - '
    ColumnSign = '| '
    space = ' '
    MiddleColumn = (ColumnSign + space * 12 + ColumnSign + space * 12 + ColumnSign)

    Line1Type = (PlusSign + (MinusSign * 4*x) + PlusSign + (MinusSign * 4*x) + PlusSign)  # Long
    Line2Type = (((ColumnSign + space * 12*x + ColumnSign + space * 12*x + ColumnSign) + '\n') * 4)  # Long

    print(Line1Type)
    print(Line2Type*y, end='')  # lat
    print(Line1Type)
    print(Line2Type*y, end='')  # lat
    print(Line1Type)

GridPrinter2(1,1)