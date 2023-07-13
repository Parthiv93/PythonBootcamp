
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print('/nWelcome to Treasure Island.')
print('/nYour mission is to find the treasure.')
a=input('/nYou are at a junction. Where do you want to go (Type "left" or "right") ? : ').lower()
if a=='right':
    print('/nOops you fell into a hole. Game over')
else:
    b=input(print('/nYou have come to a lake. There is an island at the middle of the lake. You can either swim or wait for a boat. Whats your choice ("swim" or "wait") : ')).lower()
    if b=='wait':
        print('/nYou got attacked by an angry tribe. Game over')
    else:
        c=input(print('/nYou arrived safely at the island. There\'s three doors : RED | YELLOW | GREEN . Which one do you wanna choose ? : ' )).lower()
        if c=='red':
            print('/nYou got burned by flames. Game over')
        elif c=='yellow':
            print('/nYou fell into a lave. Game over')
        else:
            print('/nCongratulations you have won. The treasure is yours')

