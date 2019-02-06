#-------------------------------------------------#
# Title: List Lab
# Dev:   Rlarge
# Date:  1/31/2019
# ChangeLog: (Who, When, What)
#   RLarge, 02/02/2019, Created Script

#-------------------------------------------------#


#!/usr/bin/env python3
# $ chmod +x dict_lab.py


#Create a dictionary containing “name”, “city”, and “cake”
# for “Chris” from “Seattle” who likes “Chocolate”
# (so the keys should be: “name”, etc, and values: “Chris”, etc.)

dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

# display dictionary
print(dict1)

# delete entry for "cake"
dict1["cake"] = ""

# display dict1
print(dict1)

# add an entry for "fruit" with "Mango"
dict1["fruit"] = "Mango"
print(dict1)

# Display the dictionary keys.
print(dict1.keys())

# Display the dictionary values.
print(dict1.values())

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("cake" in dict1)

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("Mango" in dict1.values())

# -------Dictionaries 2-------
# Using the dictionary from item 1: Make a dictionary using the same keys but
# with the number of ‘t’s in each value as the value (consider upper and lower case?).


# dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
# switch each value in dict to be the number of 't's as the value
# value 1: 0
# value 2: 2
# value 3: 1

print(dict1.values([0]))

vals = dict1.values()


dict1["name"] = "0"
dict1["city"] = "2"
dict1["cake"] = "1"
print(dict1)

# for counting
# for item in dict1.values():
#     # print(item)
#     x = item.count("t")
#     # print(x)
#     print(str(x))
#     item.replace(item, str(x))
#     # print(item)
#
# print(dict1)



# ------ Sets --------- #
# Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible by 2, 3 and 4.

# ------ Set1 --------- #
# Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible by 2, 3 and 4.

s2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3 = set([3, 6, 9, 12, 15, 18])
s4 = set([4, 8, 12, 16, 20])


print(s2)
print(s3)
print(s4)

print(s2.issubset(s3))
print(s4.issubset(s2))

# ------ Set2 --------- #

NewSet = set(["p", "y", "t", "h", "o", "n"])
NewSet.add("i")
print(NewSet)

# create frozen set with the letters in 'marathon'
fs = frozenset(("m", "a", "r", "a" "t", "h", "o", "n"))
print(fs)

# display the union and intersection of the two sets.
print("NewSet & fs sets union:", NewSet.union(fs))
print("NewSet & fs sets intersection:", NewSet.intersection(fs))