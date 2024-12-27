n=str(input("Enter employee name:"))
d=str(input("Designation:"))
s=int(input("salary:"))
specialallow=int(input("Spcall:"))
b=int(input("bonus:"))
print("Employee details")
print("---------------------")
print("Employee Name:",n)
print("Designation:",d)
print("Monthly salary:",s)
print("Special Allowances:",specialallow)
print("Bonus:",b)
#Gross Monthly salary
gms=s+specialallow
print("Gross Monthly Salary:",gms)
#gross annual salary
gas=(gms*12+b)
print("Gross annual salary:",gas)
#taxable income
if(gas>500000):
    tax=(gas*15/100)
    taxinc=gas-tax
    print("Taxable income:",taxinc)
elif(gas>400000):
    tax=(gas*10/100)
    taxinc=gas-tax
    print("Taxable income:",taxinc)
else:
    tax=(gas*2/100)
    taxinc=gas-tax
    print("Taxable income:",taxinc)
