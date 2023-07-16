import auctionbiddingart,os
print(auctionbiddingart.logo)
auction={}
bidding_finished=False
def high(bidding_record):
        highest_bid=0
        for bidder in bidding_record:
            bid_amount=bidding_record[bidder]
            if bid_amount>highest_bid:
                highest_bid=bid_amount
                winner=bidder
        print(f"The winner is {winner} with winning bid amount of ${highest_bid}")
while not bidding_finished:
    name=input("Enter the name of the bidder : ")
    bid=int(input("Enter the bid amount : $"))
    auction[name]=bid
    cont=input("Is there any other person in the room. If then type 'yes' else 'no' : ")
    os.system('cls')
    if cont=='no':
        bidding_finished=True
        high(auction)
