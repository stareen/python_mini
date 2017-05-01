n=11;  

for row in range(n):
    for j in range(row):
        x=str(j)
        print(x.rjust(len(x)),end="")
    print('')  
