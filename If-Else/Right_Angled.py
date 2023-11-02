side1 = int(input("Enter The Side 1 : - "))
side2 = int(input("Enter The Side 2 : - "))
side3 = int(input("Enter The Side 3 : - "))
hypo = 0
base = 0
height = 0
if side1 >= side2 and side1 >= side3 :
    hypo = side1
    base = side2
    height = side3
elif side2 >= side1 and side2 >= side3 :
    hypo = side2
    base = side1
    height = side3
else :
    hypo = side3
    base = side2
    height = side1

lhs = hypo ** hypo
rhs = (base**base) + (height**height)

if lhs == rhs :
    print("Right Angled Triangle")
else : 
    print("Not Right Angled Triangle")