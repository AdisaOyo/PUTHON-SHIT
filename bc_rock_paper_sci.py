import random

plays = ("rock", "paper", "scissors")

print("----------------ROCK PAPER SCISSORS----------------")


running = True
while running:
    player = None
    player = input("Enter a choice: ")
    computer = random.choice(plays)
    while player not in plays:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player = input("Enter a choice: ")

    if player == computer:
        print("----------------------OUTCOME----------------------")
        print(f"Player: {player.capitalize()} vs Computer: {computer.capitalize()}")
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("----------------------OUTCOME----------------------")
        print(f"Player: {player.capitalize()} vs Computer: {computer.capitalize()}")
        print("You win!")
    else:
        print("----------------------OUTCOME----------------------")
        print(f"Player: {player.capitalize()} vs Computer: {computer.capitalize()}")
        print("Computer wins!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

