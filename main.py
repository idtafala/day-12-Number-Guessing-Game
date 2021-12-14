#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from name import logo
import random


print(logo)
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100.")
level = ""
while not(level == 'hard' or level == 'easy' ) :
  level = input("Choose a difficulty. Type 'easy' or 'hard'")

if level == 'hard' :
  attempts = 5
else :
  attempts = 10

winning_number = random.randint(1,101)

again =True
while again == True :
  print(f"You have {attempts} remaining to guess the number.")
  guess = int(input("make a guess:"))
  if guess > winning_number :
    print("Too high.\n guess again.")
  elif guess < winning_number :
    print("Too low.\nguess again")
  else :
    print("You win !")
    again = False
  attempts -= 1
  if attempts == 0 :
    print("You lose!")
    print(f"the winning number was {winning_number}")
    again =False

