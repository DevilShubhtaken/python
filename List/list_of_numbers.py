# Write a program to make a list of all such nummbers which are divisible by 7 but are not the multiple of 5
# between 2000 - 3200 (both included). The Final list should be printed as comma-seperated sequence on a single line 

for i in range(2000 , 3201): #This Range Includes both 2600 & 3200
    if (i%7 == 0) and (i%5!=0) :
        print(f"{i},",end=" ")