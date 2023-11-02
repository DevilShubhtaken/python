#Methods in List That inceases the Length of the List

#1. Appened() : 
ls  = [4, 6, 90]
print('before Appened', ls)
ls.append(100)
ls.append("Hello")
print('After Appened ',ls)

#2. extend() : To add the elements of any seq object to the end of the object
ls = [4, 6, 10]
x = [5, 12, 30]
print('Before Extend',ls)
ls.extend(x)
print('After Extend', ls)

#3 Insert(index , value) : To Insert an element at a custom place
ls = [4, 6, 10]
ls.insert(1, 100)

#Methods In List That Decreases The Length Of The List

#1. remove() : To Remove The Item(element) with value
ls = ['Bhaskar', 'Krishnaveer', 'Manmohan', 'Ayush']
ls.remove('Manmohan')
print(ls)

#Wrtie a python program to remove all the items/elements with the given value

#2. pop() : To remove the item(element) at the last index of the given element

ls = ['Bhaskar', 'Krishnaveer', 'Manmohan', 'Ayush']
ls.pop()
print(ls)

#3. clear() : To Remove the particular element entirely from the list 
ls = ['Bhaskar', 'Krishnaveer', 'Manmohan', 'Ayush']
ls.clear('Manmohan')
print(ls)


#Methods In List That Given Index 
 
#1 index() : To give out the index of the given element in the list
ls = ['Bhaskar', 'Krishnaveer', 'Manmohan', 'Ayush']
ls.index('Manmohan')
print(ls)

#2 count() : To Count The elements inside the list
ls = ['Bhaskar', 'Krishnaveer', 'Manmohan', 'Ayush']
# ls.remove('Manmohan')
print(ls.count())


#Methods that Reaarange the Elements inside the List

#1 reverse() : To reverse the order of the List
ls = ['Bhaskar', 'Krishnaveer', 'Manmohan', 'Ayush']
ls.reverse()
print(ls)

#2 sort() : To sort the order of the List
ls = ['Bhaskar', 'Krishnaveer', 'Manmohan', 'Ayush']
ls.sort()
print(ls)

#3 copy() ; To copy the entire list and return the entire List
ls = ['Bhaskar', 'Krishnaveer', 'Manmohan', 'Ayush']
l1 = ls.copy()
print(l1)