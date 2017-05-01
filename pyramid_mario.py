# to make a pyramid for mario to jump at

input_height= int(input("Please enter the required height of the pyramid for Mario: "))

row=0
for row in range(0,input_height):
    
    spaces=9-(row+1)
    hashes=(row+1)
    row=row+1
    print((" "*spaces)+("#" * hashes)+(" "*2)+ ("#" * hashes),end='\n')
    
    
