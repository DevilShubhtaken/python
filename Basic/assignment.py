P=float(input("Enter the Principle loan amount (in Dollars)\n"))
a=float(input("Enter the Annual Interest rate\n"))
l=int(input("Enter the Loan term (in years)\n"))

r=a / 12 / 100
n=l*12

print(f"Monthly Payment(M) in dollars : {P*r*(1+r)**n/((1+r)**n-1)}")