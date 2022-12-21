import time
print("Assignment 1")
print()
print("Enter any 3 numbers")
a= float(input("1st number= "))
b= float(input("2nd number= "))
c= float(input("3rd number= "))
print((a+b+c)/3)
print()
income = int(input("Enter your Salary - "))
no_of_dependents = int(input("Enter number of dependents - "))
taxable_income= income-10000-(3000*no_of_dependents)
print("taxable income = ",taxable_income)
print("tax = ",taxable_income*0.2)
print()

no_of_seconds = int(input("number of seconds = "))
minutes = no_of_seconds//60
seconds = no_of_seconds%60
print('in minutes and seconds= ',minutes,':',seconds)
print()

time.sleep(2)

no_a= int(25)
no_b= str(25)
no_c= float(25)
sum = str(no_a+int(no_b)+no_c)

print("sum = ",sum)
print()
time.sleep(2)
import math
angle1 = 0
angle2 = 0
while angle2<=6.28320:
    a= round(math.sin(angle2),4)
    b= round(math.cos(angle2),4)
    print(angle1,'---',a,"",b)
    angle1 += 15
    angle2 += 3.14159/12
time.sleep(10)




