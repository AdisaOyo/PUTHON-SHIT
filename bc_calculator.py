# Making an entire calculator. simple calculator though

operator = input("Ener an operator (+ - * /): ")
num1 = input("Enter the first number: ")    
num2 = input("Enter the second number: ")


# This is to check if input is correct

try:
    num1 = float(num1)
except ValueError:
    num1 = input("Input valid first number!")
try:
    num1 = float(num1)
except ValueError:
    num2 = input("Input valid second number!")
if operator == "+":
    output = float(num1) + float(num2)
    print(output)
elif operator == "-":
    output = float(num1) - float(num2)
    print(output)
elif operator == "*":
    output = float(num1) * float(num2)
    print(output)
elif operator == "/":
    output = float(num1) / float(num2)
    print(output)
else:
    input("Invalid opertor! Give valid operator: ")

## If you use a try and if statement, make sure they join. If you seperate them it will not work


