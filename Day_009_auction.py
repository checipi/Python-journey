import os 

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                          
Author: Ciprian Ivanov
'''


def find_highes_bidder(bidding_dict):
    names, bets = list(bidding_dict.keys()), list(bidding_dict.values())
    bets.sort()
    highest_bet = bets[-1]
    # for x in bidding_dict:
    #     print(f"{x}: £{bidding_dict[x]}")
    for name in bidding_dict:
        if highest_bet == bidding_dict[name]:
            print(f"The winner is {name} with a bid of {bidding_dict[name]}") 


print(logo)
print("Welcome to silen bidding.")
bids = {}
continue_bid = True

while continue_bid:
    name = input("What is your name?: ").title()
    bid = int(input("What's your bid?: £"))
    bids[name] = bid
    next_bid = input("More bidders? Y/N :").lower()
    if next_bid != "y":
        find_highes_bidder(bids)
        continue_bid = False
    else:
        os.system("cls")
    
