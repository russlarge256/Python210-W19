# -------------------------- #
# Title: Warmup-1 > front_back
# Changelog:
# Russell Large, 1-16-19
# -------------------------- #


def front_back(str):
    # set up code for values less than or equal to 1
    if len(str) <= 1:
        return str

    # set up variables
    v1 = len(str)-1
    v2 = str[1:-1]

    # return value
    return str[v1] + v2 + str[0]