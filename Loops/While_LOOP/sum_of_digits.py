#Implement a program that calculates the sum of digits of a given of a given integer using a while loop 

user = int(input("Enter The Number :- "))
sum = 0
while user > 0:
    digit = user % 10
    sum = sum + digit
print(f"Sum Of the Digit : - {sum}")