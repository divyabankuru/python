n=int(input("Enter an integer:"))
if((n>=1000 and n<=9999) or (n>=-9999 and n<=-1000)):
    print("Its a four digit")
else:
    print("other")