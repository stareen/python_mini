print("\t\t\tMULTIPLICATION TABLES FROM 1 TO 12\n")
for i in range(1,13):
    for j in range(1,13):
        print(i*j,end="\t")
    print('')
    
#table of 2 to 12

for n in range(1,13):
    for i in range(1,11):
        print(" %s  X  %s = %s\n" %(n,i,n*i), end="")
    print(' ')
    
#defining a function to print a multiplication table of any integer

def table_of(x):
    for n in range(x,x+1):
        for i in range(1,11):
            print(" %s  X  %s = %s\n" %(n,i,n*i), end="")
        print(' ')

table_of(5)
