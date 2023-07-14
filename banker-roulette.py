import random
names=input('Enter the names of the persons : ')
namessplit=names.split(',')
namesget=len(namessplit)
randomnames=random.randint(0,namesget-1)
person_who_will_pay=namessplit[randomnames]
print('Person who needs to pay the bill = '+person_who_will_pay)