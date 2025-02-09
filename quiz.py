questions = ("a kerdes",
             "b kerdes",
             "c kerdes",
             "d kerdes",
             "e kerdes")
options = (("A. 1", "B. 2", "C. 3", "D. 4"),
           ("A. 4", "B. 5", "C. 6", "D. 7"),
           ("A. 1", "B. 2", "C. 3", "D. 4"),
           ("A. 1", "B. 2", "C. 3", "D. 4"),
           ("A. 1", "B. 2", "C. 3", "D. 4"))
answers = ("C""C""C""C""A")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("---------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)
    guess = input("Enter (A ,B ,C ,D ): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer ")
    question_num += 1 

print("---------------------------------")
print("            RESULTS              ")
print("---------------------------------")

print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is {score}%")