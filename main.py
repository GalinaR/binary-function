def binary(number):
  '''An implementation of the binary function that returns the binary representation of a decimal number as a string.'''
  result = ""
  if number == 0:
    print(str(number) + result)
  while number > 0:
    modulo = number % 2
    result = str(modulo) + result
    number = number // 2
  print(result)

binary(0)
binary(2)
binary(7)