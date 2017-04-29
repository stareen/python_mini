input_num=int(input("Please enter the amount needed: "))

def get_denomination():
    number = input_num
    denomination=[2000,1000,500,100,50,20,10,5,2,1]
    for x in denomination:    
        if number>=x:
            no_of_notes=number//x
            remainder=number%x
            print("The number of %s rupees notes is %s" %(x, no_of_notes))
            number=number-(x*no_of_notes)
            
get_denomination()

