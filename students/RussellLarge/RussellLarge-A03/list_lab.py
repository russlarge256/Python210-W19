#-------------------------------------------------#
# Title: List Lab
# Dev:   Rlarge
# Date:  1/26/2019
# ChangeLog: (Who, When, What)
#   RLarge, 01/26/2019, Created Script

#-------------------------------------------------#


# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
FruitList = ['Apples', 'Pears', 'Oranges','Peaches']
# Display the list (plain old print() is fine…).
print(FruitList, "\n")

# Ask the user for another fruit and add it to the end of the list.
FruitList.append(input("Please add another Fruit to the list: "))
# Display appended list
print(FruitList, "\n")

# Ask the user for a number and display the number back to the user and the
# fruit corresponding to that number (on a 1-is-first basis). Remember that
# Python uses zero-based indexing, so you will need to correct.
UserFruit = input("Please indicate what number in the Fruit List you want displayed: ")
IndexFruit = int(UserFruit)

if IndexFruit == 0:
    print("Not a valid Entry")
else:
    print(FruitList[int(UserFruit)-1], "\n")

# Add another fruit to the beginning of the list using “+” and display the list.

NewFruit = ['Blueberries']
FruitList += NewFruit
NewFruitStr = str(NewFruit)
print("Adding {}" " to the FruitList".format(str(NewFruitStr)))
print(FruitList, "\n")

# Add another fruit to the beginning of the list using insert() and display the list.

NewFruit2 = 'Apricots'
FruitList.insert(1,NewFruit2)
print("Adding {}" " to the FruitList".format(NewFruit2))
print(FruitList, "\n")

# Display all the fruits that begin with “P”, using a for loop.
print("Displaying all Fruits in FruitList that start with 'P'...")
PList = [word for word in FruitList if word[0] == 'P']
print(PList, "\n")

# --------------------------------------- Series 2 --------------------------------------------------------------- #

# Display the list.
print(FruitList, "\n")

# Remove the last fruit from the list
print("Removing the last item in the List: {}".format(FruitList[-1]))
FruitList.pop()

# Display the list.
print(FruitList, "\n")

# Ask the user for a fruit to delete, find it an delete it.
Delitem = input("Which fruit would you like to delete?")
FruitList.remove(Delitem)
print(FruitList[1:])

# --------------------------------------- Series 3 --------------------------------------------------------------- #

# Ask the user for input displaying a line like
# “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.

for item in FruitList:
    if item == ' ':
        continue
    UserAsk = input("Do you like {}? (type 'exit' to quit)".format(item).lower())
    if UserAsk == 'exit':
        print("Update complete.")
        print(FruitList[1:])
        break
    elif UserAsk == 'no':
        FruitList.remove(item)
        print(FruitList[1:])
    elif UserAsk == 'yes':
        print("ok")
        print(FruitList[1:])
    else:
        print("please answer with 'no' or 'yes'.")

# --------------------------------------- Series 4 --------------------------------------------------------------- #

# Make a new list with the contents of the original,
# but with all the letters in each item reversed.

ReverFruitItems = [x[::-1] for x in FruitList][::-1]
print("All the letters in each item reversed:")
print(ReverFruitItems)

# Delete the last item of the original list.
# Display the original list and the copy.

FruitList = FruitList[:-1]

print("Original List:{}".format(FruitList))
print("Reverse Copy:{}".format(ReverFruitItems))