## QUIZ GAME

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "What is the hottest planet in our solar system?: "
             )

options = (("A. 118", "B. 120", "C. 115", "D. 125"),
           ("A. Ostrich", "B. Emu", "C. Whale", "D. Elephant"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Argon"),   
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter")
           )

answers = ("A",
           "A",
           "B",
           "A",
           "B"
           )

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")    
    question_num += 1
print("-----------------------------")
print("RESULTS")    
print("-----------------------------")
print("Answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()
print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")