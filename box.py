input_height = int(input("Please enter the height of the pattern: "))
input_width = int(input("Please enter the width of the pattern: "))

print("+" + "-"*(input_width-2) + "+")
for i in range(input_height-2):
    print("+" + " "*(input_width-2) + "+")
print("+" + "-"*(input_width-2) + "+")
