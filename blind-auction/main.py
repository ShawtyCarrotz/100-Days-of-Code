from replit import clear

from art import logo
print(logo)
print("Welcome to the secret auction program.")

bidders_list = {}

game = True

while game == True:
  bidder_name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  bidders_list[bidder_name] = bid
  # print(bidders_list)
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no.\n").lower()

  if more_bidders == "yes":
    clear()
  if more_bidders == "no":
    game = False
    highest_bid = 0
    winner = ""
    for name in bidders_list:
      bid_amount = bidders_list[name]
      if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = name
    
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
