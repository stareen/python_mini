#printing prime numbers from 1 to 100
import math

def is_prime(n):
    if (n>2) and n%2==0:    #cannot be even
        return False
    if n in [0,1]:          #cannot be 0 or 1
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):  #cannot have factors 
        if n%i==0:
            return False
    return True         #if all 3 false then its prime

prime_list=[]
for i in range(101):
    if is_prime(i):
        prime_list.append(i)
print(prime_list)
