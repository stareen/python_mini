# to make a half pyramid for mario to jump at

input_height= int(input("Please enter the required height of the pyramid for Mario: "))

row=0
for row in range(0,input_height):
    
    spaces=9-(row+2)
    hashes=row+2
    row=row+1
    print((" "*spaces)+("#" * hashes),end='\n')
    
    
