gen = input("enter the gender of the employee(m or f):")
sal=int(input("enter the salary of the employee:"))
if(gen =='m'):
    bonus=0.05*sal
else:
    bonus=0.10*sal
if(sal<10000):
    bonus=0.02*sal
amt_to_be_paid=sal+bonus
print("salary =",sal)
print("bonus =",bonus)
print("--------------------")
print("amount to be paid:",amt_to_be_paid)
