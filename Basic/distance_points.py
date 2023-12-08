#Write An Program to find the distance two points 
import math
print("FOR POINT A")
x1 = float(input("Enter The X : - "))
y1 = float(input("Enter The Y : - "))

print("FOR POINT B")
x2 = float(input("Enter The X  : -"))
y2 = float(input("Enter The Y  : -"))

distance = math.sqrt((math.abs(x2 - x1)**2) + (math.abs(y2 - y1)**2) )