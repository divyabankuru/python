name=(input("enter student name:"))
s1=int(input("subject1 score:"))
s2=int(input("subject2 score:"))
s3=int(input("subject3 score:"))
total=0
average=0
print("student report:")
print("-----------------------------")
print("student name:", name)
print("subject1:",s1)
print("subject2:",s2)
print("subject3:",s3)
if (s1>35 and s2>35 and s3>35):
   t=s1+s2+s3
   print("total:",total)
   average=total/3
   print("average:",avg)
   print("stdent is qualified:")
   if(avg>90):
      print("congratulations you have qualified with 1st class")
   elif (avg>75):
      print("congratulations you have qualified with 2nd class") 
   else:
     print("congratulations you have qualified with 3rd class")
else:
    print("better luck next time") 
     