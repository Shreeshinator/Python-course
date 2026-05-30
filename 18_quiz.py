questions = [
    ("What is the capital of France?", ["A) Paris", "B) London", "C) Rome", "D) Berlin"], "A"),
    ("Which planet is known as the Red Planet?", ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"], "B"),
    ("What is 5 + 3?", ["A) 6", "B) 7", "C) 8", "D) 9"], "C"),
    ("Which animal is known as the King of the Jungle?", ["A) Elephant", "B) Lion", "C) Tiger", "D) Bear"], "B"),
]

score = 0
print("Quiz Game")

for number, (question, options, correct) in enumerate(questions, 1):
    print(f"{number}. {question}")
    for option in options:
        print(option)
    answer = input("Your answer: ").strip().upper()
    if answer == correct:
        score += 1
        print("Correct!")
    else:
        print("Wrong. The correct answer is", correct)
    print()

print("Quiz complete! You scored", score, "out of", len(questions))
