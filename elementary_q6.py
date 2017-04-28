num = int(input("enter any number: "))

user_option=input("Select sum or product: ")
if user_option == "sum":
    sum=0
    for i in range(num+1):
        sum=sum+i
    print("The sum of numbers from 1 to %s : %s" %(num,sum))
else:
    product=1
    for i in range(1,num+1):
        product=product*i
    print("The product of numbers from 1 to %s: %s" %(num,product))


