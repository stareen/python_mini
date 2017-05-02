n=11  
for i in range(n):
    for j in range(n-i-1):
        print(" ",end ="")
    for j in range(0,i):
        print(j,end="")
    print("")
