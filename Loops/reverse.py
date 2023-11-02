num = int(input("Enter THe Number :- "))
p = 0
for i in True:
    p = num % 10
    num = num // 10
    print(p)
    if p == 0 :
        break
