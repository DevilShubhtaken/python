#Write a program that takes an integer input from the user and counts down from that number to 1 using while loop

user = int(input("Enter The Number : - "))

while(True):
    if user == 0 :
        break;
    else:
        print(f"{user} seconds left")
        user = user - 1