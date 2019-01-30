#-------------------------------------------------#
# Title: Slicing Lab
# Dev:   Rlarge
# Date:  1/26/2019
# ChangeLog: (Who, When, What)
#   RLarge, 01/26/2019, Created Script

#-------------------------------------------------#


# -------------------- Variables ------------------------- #
numbertest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]



# -------------------- Processing ------------------------- #

def FirstLast(list):
    NewList = list[:]
    NewList[0], NewList[-1] = NewList[-1], NewList[0]
    return NewList

def EveryOther(list):
    NewList = list[:]
    v2 = NewList[0:len(list):2]
    return v2

def EveryOtherFour(list):
    NewList = list[:]
    v2 = NewList[4:-4:2]
    return v2

def ReverseElements(list):
    NewList = list[:]
    v2 = NewList[::-1]
    return v2

def FirLasMidThird(list):
    NewList = list[:]
    MiddleT = NewList[int(len(NewList)/2)]
    LastT = NewList[-3]
    FirstT = NewList[2]
    NewList = [LastT, FirstT, MiddleT]
    return NewList

# --------------------Presentation ------------------------- #

print(FirstLast(numbertest))
print(EveryOther(numbertest))
print(EveryOtherFour(numbertest))
print(ReverseElements(numbertest))
print(FirLasMidThird(numbertest))

