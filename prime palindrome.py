num=int(input("enter the number:"))
num2=str(num)
if(num2==num2[::-1]):
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime palindrome")
            break
    else:
        print(num,"yes it is a prime palindrome")
else:
    print(num,"is not a prime palindrome")