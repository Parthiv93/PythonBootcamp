import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user=int(input("What do you wanna choose - Type 1 for Rock,2 for Paper and 3 for Scissors : "))
rcs=[rock,paper,scissors]
rcsrandom=random.randint(0,len(rcs)-1)
computer=rcs[rcsrandom]
print("You have chosen : \n"+ rcs[user-1])
print("Computer has chosen : \n"+ computer)
if user==1:
   if rcsrandom==0:
    print("Its a tie")
   elif rcsrandom==1:
    print("You lost")
   else:
    print("You won")
elif user==2:
    
   if rcsrandom==0:
    print("You won")
   elif rcsrandom==1:
    print("Its a tie")
   else:
    print("You lost") 
else:
   if rcsrandom==0:
    print("You lost")
   elif rcsrandom==1:
    print("You won")
   else:
    print("Its a tie") 
