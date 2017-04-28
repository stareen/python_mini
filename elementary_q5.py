sum = 0
for i in range(17):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
print("The sum of the multiples of 3 or 5 upto 17 is = %s" % sum) 
