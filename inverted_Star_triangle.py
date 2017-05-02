input_height = int(input("Please enter the height of the pattern: "))

for i in range(input_height,0,-1):
    print(" "*(input_height-i) + "* "*(i))
