
## Inheritance in Pythons 


## --> Single / Multi-Level 
class Employee:

    company = "Adobe"
    
    def print(self):
        print("This is an Employee !!")
        
        
class Programmer(Employee):
    
    language = "Java"
    
    def print(self):
        print("This is a Programmer !!")
        
class Rahul(Programmer):
    
    brand = "Microsoft"
            
        
        
e = Employee()
p = Programmer()
r = Rahul()

print("Company : ",p.company) 
print("Lanuage : ",p.language)   
print(p.print())    
                

### --> Multiple 


class Employee:
    company = "Visa" 
    ecode = 120 
    

class Freelancer:
    company = "Fibre"
    level = 1
    
    def upgradeLevel(self):
        self.level = self.level + 1 
        
        
class Program(Freelancer,Employee):
    name = "Rahul Kumar" 
    
pr = Program() 
print(pr.company)   

print("\n")
print(r.brand)
print(r.company)
print(r.language)   


## --> super keyword        


print("\n\n")

class Person:
    country = "India"
    
    def takeBreath(self):
        print("I am breathing....")
        
            
            
class Employee(Person):
    company = "Honda"
    
    def getSalary(self):
        print(f"salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing.....")
   

e = Employee()         
e.takeBreath() 
        