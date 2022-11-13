import random, sys

# Tracking of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

# The Main Game Loop.
while True:
  print(f"{wins} Wins, {losses} Losses, {ties} Ties")
  # The Player input loop.
  while True:
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    playerMove = input()
    print("Your Move: ", playerMove)
    if playerMove == "q":
      sys.exit() # Quit the Program.
    elif playerMove == "r" or playerMove == "p" or playerMove == "s":
      break # Break out of the player input loop.
    else:
      print("Pick one of r, p, s, or q.")

# Display what the player chose:
  if playerMove == "r":
    print("ROCK versus...")
  elif playerMove == "p":
     print("PAPER versus...")
  elif playerMove == "s":
    print("SCISSORS versus...")

# Display what the computer chose:
  randomNumber = random.randint(1,3)
  if randomNumber == 1:
    computerMove = "r"
    print("ROCK")
  elif randomNumber == 2:
    computerMove = "p"
    print("PAPER")
  elif randomNumber == 3:
    computerMove = "s"
    print("SCISSORS")

# Display and record the win/loss/tie:
  if playerMove == computerMove:
    print("It is a Tie!")
    ties += 1
  elif playerMove == "r" and computerMove == "s":
    print("You Win!")
    wins += 1
  elif playerMove == "p" and computerMove == "r":
    print("You Win!")
    wins += 1
  elif playerMove == "s" and computerMove == "p":
    print("You Win!")
    wins += 1
  elif playerMove == "r" and computerMove == "p":
    print("You Lose!")
    losses += 1
  elif playerMove == "p" and computerMove == "s":
    print("You Lose!")
    losses += 1
  elif playerMove == "s" and computerMove == "r":
    print("You Lose!")
    losses += 1  