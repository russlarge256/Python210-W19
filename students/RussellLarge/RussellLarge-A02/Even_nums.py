# -------------------------- #
# Title: CodingBat: Count Evens
# Changelog:
# Russell Large, 1-23-19, created code
# -------------------------- #

def count_evens(nums):
    '''Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
    Examples:
    count_evens([2, 1, 2, 3, 4]) → 3
    count_evens([2, 2, 0]) → 3
    count_evens([1, 3, 5]) → 0
    '''

    count = 0
    for n in nums:
        count -= n % 2 - 1
    return count

# ----------- Test Code -------------- #

print(count_evens([2, 1, 2, 3, 4])) # should equal 3
print(count_evens([2, 2, 0])) # should equal 3
print(count_evens([1, 3, 5])) # should equal 0


