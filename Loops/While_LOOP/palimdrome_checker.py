#Write a program that checks if a given string is palindrome ( Reads the same forwards and backwards) Using a while loop

user = input("Enter the Number : - ")
i = len(user)
reverse = ""
while i==0:
    reverse += user.charAt(i-1)
    i -= 1
if user == reverse:
    print(f"{user} is Palimdrome")
else:
    print(f"{user} is Not Palimdrome")