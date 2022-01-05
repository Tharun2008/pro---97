import random
number = random.randint(1,9)
print("numberGuessingGame")
chanceCount=0
while(chanceCount < 7):
    questionString = int(input("enter a number between 1 and 9: "))
    if (questionString > number):
        print("your guess is too high")
    elif (questionString == number):
        print("awesome you have won")
        break
    else:
        print("your guess is too low")

        chanceCount = chanceCount + 1
    if(chanceCount > 7):
        print("you lose!!!")    
    