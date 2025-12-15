import random

secret_channel = random.randint(1, 50)
player_won = False

# Print welcome message
print("Welcome to the BBC Channel Guessing Game!")
print("I'm thinking of a channel number between 1 and 50.")
print("You have 5 tries to guess it!")

# For debugging - remove this in the final game
print(f"Secret number: {secret_channel}")

for attempt in range(5):
  user_guess = int(input("Give me a guess: "))
  
  if user_guess == secret_channel:
    print("Well done! You win!")
    player_won = True
    break
  elif user_guess < secret_channel:
    print("You guessed too low - try again.")
  else:
    print("You guess too high - try again.")


if not player_won:
  print("Sorry you lost.")
  print(f"Game over - the real answer was {secret_channel}")
else:
  print("Game over. Play again soon.")