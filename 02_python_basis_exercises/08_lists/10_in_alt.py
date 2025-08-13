destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, list):
  index = 0
  while index < len(list):
    if (list[index] == city):
      print(True)
      return
    index += 1
  print(False)


contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False