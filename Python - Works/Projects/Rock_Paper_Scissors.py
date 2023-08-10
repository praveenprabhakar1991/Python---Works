# WAP for ROCK PAPER SCISSOR Game

import random

print("***Welcome to Rock-Paper-Scissors Game***")

user_wins = 0
comp_wins = 0
ties = 0

choices = ["rock", "paper", "scissors"]

while True:
  user = input("\nChoose Rock / Paper / Scissors or 'Q' to Quit : ").lower()

  if user == "q":
    break

  if user not in choices:
    continue

  random_number = random.randint(0, 2)
  # rock : 0 , paper : 1 , scissors : 2
  comp = choices[random_number]
  print(f"\nYou Chose : {user}.")
  print(f"Computer Picked : {comp}.\n")

  if user == comp:
    print("It is a Tie")
    ties += 1

  elif user == "rock" and comp == "scissors":
    print ("You Won!")
    user_wins += 1
    
  elif user == "paper" and comp == "rock":
    print ("You Won!")
    user_wins += 1
    
  elif user == "scissors" and comp == "paper":
    print ("You Won!")
    user_wins += 1

  else:
    print("You Lose!")
    comp_wins += 1

print (f"\nYour Score : {user_wins}")
print (f"Computer Score : {comp_wins}")
print (f"Tie Score : {ties} ")
print ("\n***Thanks for playing the game***")