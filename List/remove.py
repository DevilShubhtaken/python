my_list = [1,2,3,4,5,6,7,8,9,10]
user = int(input("Enter The Number : - "))
new_list = [item for item in my_list if item != user]
print(new_list)