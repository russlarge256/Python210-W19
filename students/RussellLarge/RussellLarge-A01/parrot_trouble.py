# -------------------------- #
# Title: Warmup-1 > parrot_trouble
# Changelog:
# Russell Large, 1-16-19
# -------------------------- #


def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False
