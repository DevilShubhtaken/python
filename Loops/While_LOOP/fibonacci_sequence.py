#Write a program that generates and prints the n terms of the Fibonacci sequence using a while loop

user = int(input("Enter The Number : - "))
temp1 = 0
temp2 = 1
while True:
    print(temp1)
    print(temp2)
    temp1 = temp2
    temp2 = temp1 + temp2
    if temp2 > user:
        break