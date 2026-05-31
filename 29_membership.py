word = "APPLE"

# Membership operators: in, not in
letter = input("Enter a letter: ")
if letter in word:
    print(f"{letter} is in the word {word}.")
else:
    print(f"{letter} is not in the word {word}.")


#not in operator
if letter not in word:
    print(f"{letter} is not in the word {word}.")
else:
    print(f"{letter} is in the word {word}.")

#email demo 
email = "hello123@gmail.com"
if "@" in email and "." in email:
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
