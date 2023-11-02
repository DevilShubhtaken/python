n = 5 
i = 1
s = 0
while i<=n :
    s += i
    i += 1
print(s)

x = 'Hello World'
for i in x:
    if i == 't':
        break
    print(i,end=' ')
else:
    print('\nelse block')