n=int(input("Enter an integer:"))
if((n>=10000 and n<=99999) or (n>=-99999 and n<=-10000)):
    print("Its a five digit")
else:
    print("others")