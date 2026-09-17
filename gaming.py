import random
def rps():
    print("\n--- Rock Paper Scissors ---")
    player_score = 0
    computer_score = 0
    for i in range(1, 4):
        print("\n--- Round", i, "---")
        player1 = input("Enter Rock, Paper, or Scissors: ").lower().strip()
        player2 = random.choice(["rock", "paper", "scissors"])
        print("Computer:", player2)
        if player1 == player2:
            print("Tie")
        elif ((player1 == "rock" and player2 == "scissors") or
              (player1 == "paper" and player2 == "rock") or
              (player1 == "scissors" and player2 == "paper")):
            print("Player1 won")
            player_score += 1
        elif ((player1 == "rock" and player2 == "paper") or
              (player1 == "paper" and player2 == "scissors") or
              (player1 == "scissors" and player2 == "rock")):
            print("Player2 won")
            computer_score += 1
        else:
            print("Invalid input")
    print("\n--- FINAL SCORE ---")
    print("Player Score:", player_score)
    print("Computer Score:", computer_score)
    if player_score > computer_score:
        print("You Win!")
    elif computer_score > player_score:
        print("You Lose!")
    else:
        print("It's a Tie!")
def number_guessing():
    print("\n--- Number Guessing Game ---")
    number = random.randint(1, 10)
    for i in range(1, 4):
        print("\nChance", i)
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print("Correct! You won!")
            break
        elif guess < number:
            print("Too Low!")
        else:
            print("Too High!")
    else:
        print("\nYou used all 3 chances!")
        print("The number was:", number)
def study():
    print("\n--- Study ---")
    print("All the best! Keep learning!")
print("----- MENU -----")
print("1. Rock Paper Scissors")
print("2. Number Guessing")
print("3. Study")
choice = int(input("Enter your choice (1/2/3): "))
if choice == 1:
    rps()
elif choice == 2:
    number_guessing()
elif choice == 3:
    study()
else:
    print("Invalid choice. Please select only 1, 2, or 3.")
