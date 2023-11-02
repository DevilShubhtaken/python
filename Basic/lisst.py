myList = [9,10,11]
myList.append(12)
print(myList)

list1 = ["a","b","c"]
list2 = ["m","p","y"]
list1.extend(list2)
print(list1)

myData = ["Milk" , "TEA" , "Coffee" , "Bread"]
myData[0] = "Cold Drink"
myData[3] = "Pizza"
print(myData)

List1 = ["a" , "b" , "c"]
List2 = [1,2,3]
List3 = List1 + List2
print(List3)


newList =['apple','banana','cherry']
finalList = newList.copy()
print(finalList)


myList4 = ["a", "b", "c"]
del myList4[1]
print(myList4)

myList5 = [100,70,80,60,10]
myList5.sort()
print(myList5)


myList6 = [100,70,80,60,10]
myList6.sort(reverse = True)
print(myList6)


myList7 = ["Orange" , "banana" , "kiwi" , "cherry"]
myList7.reverse()
print(myList7)

squares = [x**2 for x in range(5)]
print(squares)

even_numbers = [x for x in range(10) if x%2 == 0]
print(even_numbers)

results = ['Pass' if score >= 60 else 'Fail' for score in [75,30,85,50]]
print(results)

names = ['John' , 'Jane' , 'Jim']
name_lengths = [len(names) for names in names]
print(name_lengths)
