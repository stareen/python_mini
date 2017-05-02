input_arrowlen = int(input("Please enter the length of the arrow: "))
input_dir = input("Please enter the direction, right or left, of the arrow: ")
if input_dir == "right":
    rt = '>'
    print("-"*(input_arrowlen) + "%s" % rt)
else:
    lt = '<'
    print("%s" % lt + "-"*(input_arrowlen))
