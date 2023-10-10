import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = str.lower((input("Please Choose an Option: Rock, Paper, or Scissors \n")))

if computer_choice == user_choice:
    print("It's a Tie")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You Win!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You Win!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You Win!")
else:
    print("You lose, computer wins.")
