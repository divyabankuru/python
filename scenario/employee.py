n=str(input("enter employee name:"))
d=str(input("enter designation:"))
s=int(input("enter salary:"))
specialallow=int(input("enter  special allowance:"))
b=int(input("bonus:"))
print("employee details")
print("---------------------------")
print("employee name:",n)
print("designation:",d)
print("salary:",s)
print("special allowance:",specialallow)
print("bonus:",b)
#gross month salary
gvs=s+specialallow
print("gross month salary:",gvs)
print("------------------------")
#gross annual salary
gas=(gvs*12+b)
print("gross annual salary:",gas)
print("---------------------------------")
#taxable income
if(gas>500000):
    tax=(gas*15/100)
    taxnic=gas-tax
    print("taxable income:,",taxnic)
elif(gas>400000):
    tax=(gas*10/100)
    taxnic=gas-tax
    print("taxable income:",taxnic)
else:
    tax=(gas*2/100)
    taxnic=gas-tax
    print("taxable income:",taxnic)    