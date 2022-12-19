## Opps in Python 


# --> Railway Class 

class RailwayForm:
    
    form = "Raiway Journey Ticket\n"
    
    def displayDetails(self):
        print(f"Name    : {self.name}")
        print(f"Tain    : {self.train}")

 
rk = RailwayForm()

rk.name = "Rahul Kumar"
rk.train = "Vikramshila Express"

print(rk.form)
rk.displayDetails()  


## --> Employeee Class 

print("\n\nEmployee \n")
class Employee:
    
    company = "Google"
    salary = 500
    
    @staticmethod   # --> self is not required 
    def greet():
        print("Good Morning !!!")
    
    

rahul = Employee()
varun = Employee()  

rahul.greet()
print(rahul.company)
print("Varun Salary : ",varun.salary)  
print("Rahul salary : ",rahul.salary)  

rahul.salary = 450
print("Updated Rahul salary : ",rahul.salary)  



## --> Constructor 

print("\n Using Constructor  : \n")
class Railway:
    
    def __init__(self,name,train,platform,birth):
        self.name = name 
        self.birth = birth
        self.train = train 
        self.platform = platform 
        
    @staticmethod   
    def greet():
        print("Welcome to Indian Raiways !!\n")
            
        
    def printDetails(self):
        print(f"Name of the Passenger  :  {self.name}")
        print(f"Name of the Train  :  {self.train}")
        print(f"Platform Number :  {self.platform}") 
        print(f"Seat Number :  {self.birth}")
        
        
tr1 = Railway("Rahul Kumar","Rajdhani Express",2,"A-21, Side Upper")
tr1.greet()
tr1.printDetails()  

tr2 = Railway("Tanisha ","Vikramshila Exp.",1,"A-22 - Side Lower")
tr2.greet()
tr2.printDetails()                      