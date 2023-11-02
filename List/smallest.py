my_list = [1,2,3,4,5,6,7,8,9]
count_even = 0
count_odd = 0
for num in my_list:
    if num%2==0:
        count_even += 1
    else :
        count_odd += 1
print("Even Count : - ",count_even)
print("Odd Count : - ",count_odd)