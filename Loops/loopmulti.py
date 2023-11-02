n = int(input("Enter A Positive Number : - "))
m = 1
if n <= 0 :
    print("DO NOT ENTER SUCH NUMBERS")
else :
    for i in range(1,11):
        m = n*i
        print(n," x ",i," = ",m)