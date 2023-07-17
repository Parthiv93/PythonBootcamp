import blackjackart,random
print (blackjackart.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards=[]
computer_cards=[]
def deal_card():
    rand_card=random.choice(cards)
    return rand_card
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
print(user_cards)
print(computer_cards)
        