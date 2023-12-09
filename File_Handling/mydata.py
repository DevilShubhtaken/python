# Write a program to create a new file name 'mydata.txt' and 
# write your name, phone no., roll no. and your branch seperated by space

name = input("Enter Name : - ")
phone = int(input("Enter Phone No. : - "))
roll = int(input("Enter Roll. No. : - "))
branch = input("Enter Branch : - ")

with open('mydata.txt', 'w') as file:
    file.write(f"Name : {name} Phone No. : {phone} Roll No. : {roll} Branch : {branch}")