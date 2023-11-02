list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9,10]
union = []
for item in list1 + list2 :
    if item not in union :
        union.append(item)