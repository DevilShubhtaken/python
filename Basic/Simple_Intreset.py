#Write a program to find The Simple Intrest And The total amount when the principle, Rate of Intreset and time 
#are enterd by the user

principle_Amount = float(input("Enter The Principle Amount : - "))
rate_of_intrest = float(input("Enter The Rate Of Intrest : - "))
time_of_intrest = float(input("Enter The Duration : - "))
simple_intrest = (principle_Amount * rate_of_intrest * time_of_intrest)/100
print(f"Simple Intrest : - {simple_intrest}")