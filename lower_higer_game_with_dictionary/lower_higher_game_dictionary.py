from random import randint
import os
from data import game_data
from logos import game_logo
from logos import vs_logo

def random_item(list):
    """Returns a random number in range 0 and the length of a list - 1."""
    item = randint(0, len(list) - 1 )
    return item

def get_info(number, list_item):
    """Gets an number and a list of dictionaries and returns an f-string with the items 
    and the numbers of followers as a separate value."""
    name_a = list_item[number].get('name')
    followers_a = list_item[number].get('follower_count')
    description_a = list_item[number].get('description')
    country_a = list_item[number].get('country')    
    return f"{name_a}, {description_a}, from {country_a}", followers_a

score = 0
item_one = random_item(game_data)

while True:
    print(game_logo)
    if score > 0:
        print("Score", score)
    item_two = random_item(game_data)
    while item_one == item_two:
        item_two = random_item(game_data)
    names_a, followers_a = get_info(item_one, game_data)
    names_b, followers_b = get_info(item_two, game_data)     
    print("Compare A: ", names_a)
    print(vs_logo)
    print("Compare B:", names_b)

    user_choice = input("Who has more followers? Type 'A' or 'B':  ").lower()

    if user_choice == 'a' and followers_a > followers_b:
        score += 1
    elif user_choice == 'b' and followers_a < followers_b:
        score += 1
    else:
        os.system('cls')
        print(game_logo)
        print("Sorry, that was wrong. Final score:", score)
        continue_game = input("Do you want to try again? Type 'y' or 'n': ").lower()
        if continue_game == "y":
            os.system('cls')
            #low_high()
        else:
            print("Goodbye!")
            break
        
    item_one = item_two
    os.system('cls')
        
