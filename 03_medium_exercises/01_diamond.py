def flank_maker(length):
  if (length % 2 == 1):
    return ' ' * ((length // 2) + 1)
  else:
    return ' ' *  (length // 2)

def diamond(startingLetter):
  flank = flank_maker(len(curr))
  if letter == 'A':
    print('A')
    return
  width = ord(letter) - ord('A') + 1
  flank = flank_maker(width)
  print(len(flank))

diamond('A')
diamond('B')
diamond('C')
diamond('D')