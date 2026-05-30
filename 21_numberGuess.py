import random

min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))

answer = random.randint(min, max)
guesses = 0

is_running = True

print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {min} and {max}.")

while is_running:
    guess = int(input("Enter your guess: "))
    guesses += 1
    
    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {answer} in {guesses} guesses!")
        is_running = False