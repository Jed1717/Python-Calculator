import sys

while True:

# Variables

  currentsymbol = input("Add, subtract, multiply, divide? > ")
  
  if currentsymbol == "quit" or currentsymbol == "exit":
    sys.exit()
    
  # Tell user Num1 and Num2
  
  Num1 = input("Type Number 1: ")
  while not Num1.replace('.', '', 1).isdigit():  # Check if it's a valid float input
      Num1 = input("Please enter a valid number for Number 1: ")

  Num2 = input("Type Number 2: ")
  while not Num2.replace('.', '', 1).isdigit():  # Check if it's a valid float input
      Num2 = input("Please enter a valid number for Number 2: ")
  
  # Sum Num1 and Num2
  
  currentsymbol = currentsymbol.lower()
  if currentsymbol == "add":
    Sum = float(Num1) + float(Num2)                                                  
    print("Your answer to " + str(Num1) + " + " + str(Num2) + " is " + str(Sum))
  elif currentsymbol == "subtract":
    Sum = float(Num1) - float(Num2)                                                  
    print("Your answer to " + str(Num1) + " - " + str(Num2) + " is " + str(Sum))
  elif currentsymbol == "multiply":
    Sum = float(Num1) * float(Num2)                                                  
    print("Your answer to " + str(Num1) + " * " + str(Num2) + " is " + str(Sum))
  elif currentsymbol == "divide":
    Sum = float(Num1) / float(Num2)                                                  
    print("Your answer to " + str(Num1) + " ÷ " + str(Num2) + " is " + str(Sum))

  else:
    print("Selected operation not valid, try another one...")