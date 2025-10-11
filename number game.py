import random
number=random.randint(1,10)
guess=int(input("guess a number between 1 and 10"))
if guess==number:
   print("you guessed it right")
else:
    print("you guessed it wrong")    