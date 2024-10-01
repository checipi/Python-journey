import random
import os

# Number Guessing Game

# A random number form 1 to 100 is chosen
number = random.choice(range(1, 101))
print("The number to be guessed: ", number)

# User chooses a number
choice = int(input("Choose a number: "))
print(f"Number {number}\nGuess {choice}")

if choice < number:
    print("Too low")
    choice = choice
    print(choice)
elif choice > number:
    print("Too high")
else:
    if choice ==  number:
        print("You win")
        