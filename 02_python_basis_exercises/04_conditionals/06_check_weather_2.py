weather = 'foggy'
match weather:
  case 'foggy':
    print("it's foggy out")
  case 'sunny':
    print("it's sunny")
  case 'rainy':
    print("it's rainy")
  case _:
    print("Let's stay inside.")
