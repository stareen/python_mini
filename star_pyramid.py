input_height = int(input("Please enter the height of the pattern: "))

for i in range(input_height):
    print(" "*(input_height-i-1) + "* "*(i+1))

for j in range(input_height-1,0,-1):
    print(" "*(input_height-j) + "* "*(j))
