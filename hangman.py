import random
words=["transformers","avengers","batman","oppenheimer","barbie"]
blank=[]
randchose=random.choice(words)
wordlen=len(randchose)
for i in range(wordlen):
    blank.append("_")
print("Welcome to hangman movie guesser. You have to guess the movie before the man gets hanged")
guessword=input("Guess any letter : ").lower()
for i in range(wordlen):
    letter=randchose[i]
    if letter==guessword:
        blank[i]=letter
print(blank)