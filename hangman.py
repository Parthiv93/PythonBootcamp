import random
words=["transformers","avengers","batman","oppenheimer","barbie"]
blank=[]
randchose=random.choice(words)
wordlen=len(randchose)
for i in range(wordlen):
    blank.append("_")
print("Welcome to hangman movie guesser. You have to guess the movie before the man gets hanged")
print("Guess the blank spaces of the letters of the movie below")
print(blank)
endofgame=False
while(not endofgame):
    guessword=input("Insert any letter : ").lower()
    for i in range(wordlen):
        letter=randchose[i]
        if letter==guessword:
            blank[i]=letter
    print(blank)
    if "_" not in blank:
        endofgame=True
        print("You won")
        