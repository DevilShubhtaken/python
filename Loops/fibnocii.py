a = 0
b = 1
c = 2
t = 0
num = int(input("Enter The Number : - "))
print(a)
print(b)
while c<num+1 :
    t = a+b
    print(t)
    a = b
    b = t
    c = c+1