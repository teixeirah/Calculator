import sys

while True:
  operador = None
  num1 = None
  num2 = None
  res = None
  final = None
  print("\nTHIS-IS-A-CALCULATOR")
  print("-> Type '+' to add '2' numbers")
  print("-> Type '-' to subtract '2' numbers")
  print("-> Type '*' to multiply '2' numbers")
  print("-> Type '/' to divide '2' numbers")
  print("-> Type 'off' to turn-off the calculator")
  operador = input("-> ")
  if operador == "+":
    print("Operator -> Adding")
    print("-> Type the first number you want to add")
    num1 = float(input("-> "))
    print("Type the number you want to add " + str(num1) + " with")
    num2 = float(input("-> "))
    res = float(num1) + num2
    final = str(num1) + " plus " + str(num2) + " is equal to: " + str(res)
    print(final)
  if operador == "-":
    print("Operator -> Subtracting")
    print("-> Type the first number you want to subtract")
    num1 = float(input("-> "))
    print("Type the number you want to subtract " + str(num1) + " with")
    num2 = float(input("-> "))
    res = float(num1) - num2
    final = str(num1) + " minus " + str(num2) + " is equal to: " + str(res)
    print(final)
  if operador == "*":
    print("Operator -> Multiplying")
    print("-> Type the first number you want to multiply")
    num1 = float(input("-> "))
    print("Type the number you want to multiply " + str(num1) + " with")
    num2 = float(input("-> "))
    res = float(num1) * num2
    final = str(num1) + " times " + str(num2) + " is equal to: " + str(res)
    print(final)
  if operador == "/":
    print("Operator -> Dividing")
    print("-> Type the first number you want to divide")
    num1 = float(input("-> "))
    print("Type the number you want to divide " + str(num1) + " with")
    num2 = float(input("-> "))
    res = float(num1) / num2
    final = str(num1) + " divided by " + str(num2) + " is equal to: " + str(res)
    print(final)
  if operador == "off":
    break
    sys.exit()
