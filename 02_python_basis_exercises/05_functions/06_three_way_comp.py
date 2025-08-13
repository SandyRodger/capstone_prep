print("Triangle" if (1 * 3) == 3 else "Square")

def compare_by_length(s1, s2):
  if len(s1) > len(s2):
    return 1
  elif len(s2) > len(s1):
    return -1
  else:
    return 0
  
print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0