Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>starting_bid= int(input("What would you like the starting bid to be?"))
bid=int(input("What would you like to bid?"))
while True:
    if (int(bid))>(int(starting_bid)):
        print("You have won the auction")
        break
    else: 
        bid=input("Bid is too low what would you like to bid?")
print ("Congrats you have won the auction payment is expected in 24 hours!")
... 
