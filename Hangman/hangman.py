import random
import hangmanart
lives=6
words=["transformers","avengers","batman","oppenheimer","barbie"]
blank=[]
randchose=random.choice(words)
wordlen=len(randchose)
for i in range(wordlen):
    blank.append("_")
print(hangmanart.logo)
print("Welcome to hangman movie guesser. You have to guess the movie before the man gets hanged")
print(hangmanart.stages[0])
print("Guess the blank spaces of the letters of the movie below")
print(blank)
endofgame=False
while(not endofgame):
    guessword=input("Insert any letter : ").lower()
    for i in range(wordlen):
        letter=randchose[i]
        if letter==guessword:
            blank[i]=letter
    if guessword not in randchose:
            print(guessword+" not in the name of the movie. You lost 1 life")
            lives-=1
            if lives==0:
               endofgame=True
               print("You lost, the man got hanged :(")
            else:
               print(hangmanart.stages[len(hangmanart.stages)-lives])
    print(blank)
    if "_" not in blank:
        endofgame=True
        print("You won")
        