#Write a program that calculates the factorial of given positive integer using while loop

user = int(input("Enter The Number : - "))
factorial = 1
while(user > 0):
    factorial = factorial * user
    user = user - 1