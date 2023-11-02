p = int(input("Enter the Number : -"))
a = p
su = 0
r = 0
while (p<0):
    r = p/10
    p = p%10
    su = su + (r*r*r)
if su==a :
    print(a," is a Armstrong Number")
else :
    print(a," is not a Armstrong NUmber")