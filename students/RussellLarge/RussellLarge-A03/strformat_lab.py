#-------------------------------------------------#
# Title: String Format Lab
# Dev:   Rlarge
# Date:  1/26/2019
# ChangeLog: (Who, When, What)
#   RLarge, 01/26/2019, Created Script

#-------------------------------------------------#

# -------------------- Variables ------------------------- #
# Task 1 & 2 & 3 #
TupleTask = (2, 123.4567, 10000, 12345.67)

# Task 3 #
numbertest = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

# Task 4 #
NewTup = 4, 30, 2017, 2, 27

# -------------------- Processing ------------------------- #

# -------------------- Task 1 & 2 ----------------- #

FirstTuple = "file_00{}".format(TupleTask[0])
SecondTuple = "{}".format(round(TupleTask[1], 2))
ThirdTuple = "{:.2e}".format(TupleTask[2])
FourthTuple = "{:.3e}".format(TupleTask[3])

TaskOne = FirstTuple, SecondTuple, ThirdTuple, FourthTuple
TaskTwo = f"('{FirstTuple}', '{SecondTuple}', '{ThirdTuple}', '{FourthTuple}')"
AnotherFormat = "('{}', '{}', '{}', '{}')".format(FirstTuple, SecondTuple, ThirdTuple, FourthTuple)

# -------------------- Task 3 ----------------- #

def NumberDisplay(in_tuple):
     # make a format string
     TupLen = len(in_tuple)
     return "The {} numbers are: {}".format(TupLen, in_tuple)

# -------------------- Task 4 ----------------- #


def NewTupDisplay(list):
    ReForm1 = list[0] - 2
    TupIndex1 = "0{}".format(ReForm1)
    TupIndex2 = list[1] - 3
    TupIndex3 = list[2]
    ReForm2 = list[3] + 2
    TupIndex4 = "0{}".format(ReForm2)
    TupIndex5 = list[4] + 3
    return "'{}, {}, {}, {}, {}'".format(TupIndex1, TupIndex2, TupIndex3, TupIndex4, TupIndex5)


# --------------------Presentation ------------------------- #


# Task 1 & 2
print(TupleTask)
print(TaskOne)
print(TaskTwo)
print(AnotherFormat)

# Task 3
print(NumberDisplay(TupleTask))
print(NumberDisplay(numbertest))

# Task 4
print(NewTupDisplay(NewTup))

