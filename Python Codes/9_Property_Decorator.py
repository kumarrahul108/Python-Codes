## Property Decorator in Python 


# Method - 1
class Employee1:
    
    company = "Google"
    salary = 400
    location = "New Delhi"
    
    def changeSalary(self,sal):
        self.salary = sal 
        
        
e = Employee1()
print("Method - 1 :")
print(e.company)
print("Older : ",e.salary)        
e.changeSalary(500)
print("Newer : ",e.salary)
print("Employe cLass Salary : ",Employee1.salary)


print("\n Method - 2")

class Employee2:
    
    company = "Google"
    salary = 400
    location = "New Delhi"
    
    
    def changeSalary(self,sal):
        self.__class__.salary = sal 
        

e2 = Employee2()
print("Method - 1 :")
print(e2.company)
print("Older : ",e2.salary)        
e2.changeSalary(500)
print("Newer : ",e2.salary)
print("Employe cLass Salary : ",Employee2.salary)


print("Method - 3 :")


class Employee3:
    
    company = "Google"
    salary = 400
    location = "New Delhi"
    
    @classmethod
    def changeSalary(self,sal):
        self.salary = sal
        
        

e3 = Employee3()
print("Method - 1 :")
print(e3.company)
print("Older : ",e3.salary)        
e3.changeSalary(500)
print("Newer : ",e3.salary)
print("Employe cLass Salary : ",Employee3.salary)
         
        

### Getter & Setters In Python :


class BharatGas:
    
    company = "H.P."
    salary = 5600
    salarybonus = 500
    
    # getter method 
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    # setter method 
    @totalSalary.setter
    
    def totalSalary(self,sal):
        self.salarybonus = sal - self.salary
        
        
b = BharatGas()

b.totalSalary = 7800

print("\n\n")
print("Total Salary :  ",b.totalSalary)

print("Salary  :  ",b.salary)

print("Bonus :  ",b.salarybonus)

       

## Operators OverLOadding 


print("Operators OverLoading :  ")
class Number:
    
    def __init__(self,num):
        self.num= num 

    def __add__(self,num2):     
        print("Let's Add !!") 
        return self.num + num2.num 
    
    def __mul__(Self,num2):
        return self.num*num2.num 
    
    
n1 = Number(4)
n2 = Number(6)    

sum = n1 + n2
print("Sum :  ",sum) 

mul = n1 * n2 
print("Multiplication : ",mul) 
           