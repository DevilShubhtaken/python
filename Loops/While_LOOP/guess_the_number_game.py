#Create a simple number guessing game where the computer selects a random number between 1 to 100, 
#user has to guess it. Use a while loop to keep the game running until the user guesses correctly 

import random
user = int(input("Enter A Number b/w 1 - 100 : - "))
random_number = random.randint(1, 100)
while True:
    if user == random_number:
        print(f"{user} is the right number")
        print("YOU HAVE WON THE GAME!!!")
        break
    else:
        print("WRONG CHOICE!!!")
        print("TRY AGAIN!!!")
        user = int(input("Enter A Number b/w 1 - 100 : - "))