#Write a program that takes an input from the user and prints its multiplication table from 1 - 10 using a while loop

user = int(input("Enter The Number : - "))
i = 1
while i<11 :
    print(f"{user} x {i} = {user*i}")
    i += 1