def is_empty(s): return not s

def is_empty_or_blank(str):
  return (is_empty(str) | str.isspace())

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True