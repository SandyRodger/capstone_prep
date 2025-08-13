# def starts_with(string, substring):
#   index = 0
#   while index < len(substring):
#     if string[index] != substring[index]:
#       return False
#     index += 1
#   return True

def starts_with(string, substring):
  return string.startswith(substring)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
print(starts_with("school", "ool"))  # False