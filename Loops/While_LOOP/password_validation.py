#Implement a program that asks the user to enter the password and keeps asking until the correct 
#password is entered. Use a while loop for this 

user = 0
code = 0000
while True:
    if user == code:
        print("BRO, YOU GOT THE CODE!!!")
    else:
        print("TRY AGAIN!!!")
        user = int(input("Enter the 4-digit Passcode : -"))