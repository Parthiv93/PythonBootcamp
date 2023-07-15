import random
words=["transformers","avengers","batman","oppenheimer","barbie"]
randchose=random.randint(0,len(words)-1)
wordchose=words[randchose]
print("Welcome to hangman movie guesser. You have to guess the movie before the man gets hanged")
guessword=input("Guess any letter : ")
for i in wordchose:
    if i==guessword:
        print("true")
    else:
        print("false")
        