operator = input("Enter an operator (+, -, *, /): ")
if operator not in ["+", "-", "*", "/"]:
    print("Invalid operator. Please enter one of the following: +, -, *, /.")
    exit()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {round(result, 2)}")

elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {round(result, 2)}")

elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {round(result, 2)}")

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {round(result, 2)}")
    else:
        print("Error: Division by zero is not allowed.")

else: 
    print("Invalid operator. Please enter one of the following: +, -, *, /.")
