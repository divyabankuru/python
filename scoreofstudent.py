name=str(input("Enter student name:"))
s1=int(input("subject 1 score:"))
s2=int(input("subject 2 score:"))
s3=int(input("subject 3 score:"))
print("Student Report card")
print("----------------------")
print("Student Name",name)
print("Subject1",s1)
print("Subject2:",s2)
print("Subject3:",s3)
if s1>35 and s2>35 and s3>35:
    t=s1+s2+s3
    print("Total score:",t)
    avg=t/3
    print("Average:",avg)                 
    print("student is qualified")
    if(avg>90):
        print("congratulations you have qualified with 1st class")
    elif(avg>75):
        print("congratulations you have qualified with 2nd class")
    else:
        print("congratulations you have qualified with 3rd class")
else:
    print("Better luck next time")
     
