import textwrap

n=11;  
for i in range(n):  
    for j in range(i):
        initial_indent = ' '*(n-j)
        wrapper= textwrap.TextWrapper(initial_indent=initial_indent,width=10) 
        print (wrapper.fill(j))
     

