n = int(input("Enter A Positive Number : - "))
sum_of_even = 0
sum_of_odd = 0
for i in range(1,n+1):
    if (i%2==0) :
        sum_of_even = sum_of_even + i
    else :
        sum_of_odd =sum_of_even + i
for i in range(1,n+1):
    if (i%2==0) :
        sum_of_even = sum_of_even + i
    else :
        sum_of_odd =sum_of_even + i
print("The Sum of first ",n,"even natural numbers is ",sum_of_even)
print("The Sum of first ",n,"odd natural numbers is ",sum_of_odd)