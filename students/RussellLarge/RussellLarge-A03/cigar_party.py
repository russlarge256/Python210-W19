'''
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
'''

def cigar_party(cigars, is_weekend):
  # cigars is True if cigars is >40 and <60
  # return True if cigars >60
  if cigars >= 40 and cigars <= 60:
      return True
  elif is_weekend == True and cigars > 60:
      return True
  else:
      return False


print(cigar_party(61, False))
print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))