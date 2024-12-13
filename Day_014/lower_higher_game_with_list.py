from random import randint
import os

GAME_LOGO = """
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                            
██╗      ██████╗ ██╗    ██╗███████╗██████╗  
██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗ 
██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝ 
██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗ 
███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║ 
╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝ 
"""
VS_LOGO = """
██╗   ██╗███████╗
██║   ██║██╔════╝
██║   ██║███████╗
╚██╗ ██╔╝╚════██║
 ╚████╔╝ ███████║
  ╚═══╝  ╚══════╝
"""
LIST_OF_ITEMS = [
    "Reincarnation",
    "Berlin Wall",
    "Uranus, a planet",
    "Climate change",
    "Maradona, a retired football player",
    "Prosecco, a type of sparkling wine",
    "Mastercard",
    "Johnny Cash, american singer and song writer",
    "Taj Mahal, a famous mausoleum from India",
    "Shih Tzu, a small dog breed",
    "Maltese, a dog breed",
    "Serena Williams, a tenis player",
    "Kanie West, a music singer and producer",
    "Mancheste City, a football team from England",
    "Mancheste United, a football team from England",
    "Hotmail, a free web-based email service",
]

def random_item(list):
    item = randint(0, len(list) - 1 )
    return item



def low_high():
    score = 0
    item_one = random_item(LIST_OF_ITEMS)

    while True:
        print(GAME_LOGO)
        if score > 0:
            print("Score", score)
        item_two = random_item(LIST_OF_ITEMS)
        while item_one == item_two:
            item_two = random_item(LIST_OF_ITEMS)
            
        print("Compare A:", LIST_OF_ITEMS[item_one])
        print(VS_LOGO)
        print("Compare B:", LIST_OF_ITEMS[item_two])

        user_choice = input("Who has more searches? Type 'A' or 'B':  ").lower()

        if user_choice == 'a' and item_one > item_two:
            score += 1
        elif user_choice == 'b' and item_one < item_two:
            score += 1
        else:
            os.system('cls')
            print(GAME_LOGO)
            print("Sorry, that was wrong. Final score:", score)
            continue_game = input("Do you want to try again? Type 'y' or 'n': ").lower()
            if continue_game == "y":
                os.system('cls')
                low_high()
            else:
                print("Goodbye!")
                break
            
        item_one = item_two
        os.system('cls')
            
low_high()
