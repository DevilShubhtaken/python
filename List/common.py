my_list = [1,2,3,4,5]
my_list2 = [4,5,6,7,8,9]
inter = []
for num in my_list :
    if num in my_list2 and num not in inter:
        inter.append(num)
print(inter)