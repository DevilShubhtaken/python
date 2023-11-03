# Write a Python program that takes a starting and ending number as input from the user. The Program should print all the numbers from 
# the starting to the ending number, following there rules :

# If the Number is divisible by 2, print "Good"
# If the Number is divisible by 3, print "Student"
# If the Number is divisible by 2 and 3, print "Good Student!"
# Otherwise, simply print the number itself.

starting_num = int(input("Enter The Starting Number : - "))
ending_num = int(input("Enter The Ending Number : - "))
for i in range(starting_num , ending_num +1) :
    if i%2 == 0 and i%3 == 0 :
        print(i, ":", "Good Student!!")
    elif i%2 == 0 :
        print(i, ":", "Good")
    elif i%3 == 0 :
        print(i, ":", "Student")
    else :
        print(i)