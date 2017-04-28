input_num=int(input("Please enter the amount needed: "))

if input_num>=2000:
    two_thousands=input_num//2000
    rem_thousands=input_num%2000
    print("The number of 2000 rupees notes is %s" % two_thousands)
if input_num<2000:
    one_thousands=input_num//1000
    rem_hundreds=input_num%1000
    print("The number of 1000 rupees notes is %s." % one_thousands)
else:
    one_thousands=rem_thousands//1000
    rem_hundreds=rem_thousands%1000
    print("The number of 1000 rupees notes is %s." % one_thousands)

if rem_hundreds>=500:
    five_hundreds=rem_hundreds//500
    rem_hundreds1=rem_hundreds%500
    print("The number of 500 rupees notes is %s" % five_hundreds)
if rem_hundreds<500:
    one_hundreds=rem_hundreds//100
    rem_tens=rem_hundreds%100
    print("The number of 100 rupees notes is %s." % one_hundreds)
else:
    one_hundreds=rem_hundreds1//100
    rem_tens=rem_hundreds1%100
    print("The number of 100 rupees notes is %s." % one_hundreds)

if rem_tens>=50:
    fiftys=rem_tens//50
    rem_tens1=rem_tens%50
    print("The number of 50 rupees notes is %s" % fiftys)
if rem_tens<50:
    twentys=rem_tens//20
    rem=rem_tens%20
    print("The number of 20 rupees notes is %s." % twentys)
elif rem_tens1 in range(20,50):
    twentys=rem_tens1//20
    rem=rem_tens1%20
    print("The number of 20 rupees notes is %s." % twentys)
if rem<20:
    tens=rem//10
    print("The number of 10 rupees notes is %s." % tens)
    
