# -------------------------- #
# Title: Task 1: Explore Errors
# Changelog (who, when, what):
# Russell Large, 1-17-18, created
# -------------------------- #

def NameError():
    try:
      NameError()
    except:
      print("local/global name not found. applies only to unqualified names.\n")

def TypeError():
   try:
     TypeError()
   except:
     print("operation/function applied to an object of inappropriate type.\n")

def SyntaxError():
  try:
    SyntaxError()
  except:
    print("parser encountered a syntax error.\n")

def AttributeError():
  try:
    AttributeError()
  except:
    print("attribute reference failed.\n")


NameError()
TypeError()
SyntaxError()
AttributeError()