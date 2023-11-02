my_list = [1,2,3,4,5, 5, 7,6,7,8,9]
unique_list = []

for num in my_list:
    if num not in unique_list :
        unique_list.append(num)

print("List after removing duplicates : - ",unique_list)