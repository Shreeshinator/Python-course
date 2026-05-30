#logical operators help in combining multiple conditions in a single statement. The three main logical operators in Python are:
#1. and: Returns True if both conditions are true.
#2. or: Returns True if at least one of the conditions is true.
#3. not: Returns True if the condition is false (negates the condition).

#Example 1: Using 'and' operator
age = 25
if age >= 18 and age <= 30:
    print("You are eligible for the youth program.")

#Example 2: Using 'or' operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
    
#Example 3: Using 'not' operator
is_raining = False
if not is_raining:
    print("You can go outside without an umbrella.")

