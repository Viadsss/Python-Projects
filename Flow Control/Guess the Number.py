import random, sys

# Tracking of Correct Guesses.
correctGuess = 0

while True:
  print(f"You already guessed {correctGuess} times!")
  # The Player Input Loop.
  while True:
    print('Do you want to Guess my number?')
    print('Type [Y] to play and [N] to not continue')
    playerOption = input()
    if playerOption == 'N':
      sys.exit() # Quit the Program.
    elif playerOption == "Y":
      break # Break out of the player input loop.
    else:
      print('Cnoose [Y] or [N]')



  # Generate a number for the user to guess.
  secretNum = random.randint(1,20)
  print('Guess the number between 1 and 20')

  # Ask the player to guess 5 times
  for guessTaken in range(1,6):
    print('I am thinking of a number between 1 and 20, Guess it!')
    guess = int(input())

    if guess > secretNum:
      print('Your guess is to High.')
    elif guess < secretNum:
      print('Your guess is to low.')
    else:
      break # This condition is the correct guess

  if guess == secretNum:
    correctGuess += 1
    print(f"Good Job! You guessed my number in {guessTaken} guesses!\n")
  else:
    print(f"Nope. The number I am thinking of was {secretNum}\n")