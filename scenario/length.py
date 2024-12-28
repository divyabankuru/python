list=['divya','gayathri','nagu','sangee','chaitu','vyshu','swetha','bhavya']
for i in list:
    if(len(i)==5):
        print(i)
print("------------------------")
print(min(list))
print(max(list))
print("----------------------------------------------")
print("before sorting:",list)
list.sort()
print("after sorting;",list)
list.reverse()
print(list)

