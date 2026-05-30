response = input("Enter a number: ")
number = int(response)
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")    
else:
    print("You entered zero.")