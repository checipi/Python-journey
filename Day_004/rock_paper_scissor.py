rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import randint
x = 0
while x < 5:
    print("Welcome to Rock, Paper, Scissors game. For Rock press 1.\nFor Paper press 2 and for Scissors press 3.")
    rps = [rock, paper, scissors]
    user_input = int(input())
    bot_choice = randint(0, 2)
    print(f"Your choice:\n{rps[user_input - 1]}")
    print(f"Computer choice:\n{rps[bot_choice]}")
    print("User: " + str(user_input) + " Bot: " + str(bot_choice + 1))
    if user_input == bot_choice + 1:
        print("Draw")
    elif user_input == 2 and bot_choice + 1 == 1:
        print("You win!")
    elif user_input == 3 and bot_choice + 1 == 2:
        print("You win!")
    elif user_input == 1 and bot_choice + 1 == 3:
        print("You win!")
    else:
        print("You lose!")
    x += 1
