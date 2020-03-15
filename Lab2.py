def MinElem():
  try:
    a = float(input("Enter a value: "))
    b = float(input("Enter b value: "))
    if a == b: 
      print("Element are equal.")
      return
    Arr = [a, b]
    print("Min element is: ", min(Arr))
  
  except ValueError:
    print("\n", "Error: invalid input value.")
    print(" Data must be numeric!")

MinElem()
