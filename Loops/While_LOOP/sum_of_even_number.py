#Write a program that calculates the sum of all the even numbers from 1 to n,
#where n is an integer input by the user, using a while loop 

user = int(input("Enter The Number : - "))
sum = 0
while user!=0:
    if user%2==0:
        sum = sum + user
    user -= 1
print(f"Sum : - {sum}")