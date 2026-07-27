import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {lowest_num} and {highest_num}. Can you guess it?")
print(f"Select a number between {lowest_num} and {highest_num}.")
while is_running:
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print(f"Please enter a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {answer} in {guesses} guesses!")
            is_running = False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print(answer)  # This line is for testing purposes. Remove it in the final version.
