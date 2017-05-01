import math

input_dollars=float(input("O hai! how much change is owed: "))
    
input_cents=round((input_dollars*100),2)
coins=[25,10,5,1]
for x in coins:
     if input_cents>x:
        no_of_coins=input_cents//x
        rem_amount=input_cents%x
        print("The number of %i coins is %i" %(x, no_of_coins))
        input_cents=input_cents-(x*no_of_coins)


