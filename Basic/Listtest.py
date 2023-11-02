myList = [10,20,30,40,50,60,70,100]
user  = int(input("Enter The Number : - "))
print(myList[3])
print(myList[-1])
sublist = myList[1:5]
myList[2] = 10
#myList.append(20)
length = len(myList)
myList[length - 1] = user
del myList[0]
myList.insert(1,5)
print(myList)