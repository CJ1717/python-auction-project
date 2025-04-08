starting_bid = int(input("What would you like the starting bid to be?"))
bid = int(input("What would you like to bid?"))
while True:
    if (int(bid)) > (int(starting_bid)):
        print("You have won the auction")
        break
    else: 
        bid = input("Bid is too low what would you like to bid?")
print("Congrats you have won the auction payment is expected in 24 hours!")
