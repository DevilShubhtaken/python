side1 = int(input("Enter The Side 1 : - "))
side2 = int(input("Enter The Side 2 : - "))
side3 = int(input("Enter The Side 3 : - "))
if side1==side2 == side3:
    print("Equilateral Triangle")
elif (side1 == side2) or (side1 == side3) or (side2 == side3):
    print("Isosceles Triangle")
else :
    print("Scalene Triangle")