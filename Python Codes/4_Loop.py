
### Looping Execution 

i = 1
while i<=5:
    print("Rahul Kumar")
    i += 1
    

print("\n\n")    
fruits = ['Banana','Mango','Guavava','Coconut','Watermelon','Litchi']
j = 0
while j < len(fruits):
    print(fruits[j])
    j += 1
    
    
fruit2 = ['Banana','Mango','Guavava','Coconut','Watermelon','Litchi']    
print("\n\n")    
for item in fruit2:
    print(item)   
    
    
print("\n\n")

for i in range(1,11,1):
    print(i)
    

print("\n\n\n")
for i in range(1,11):
    print(i)  
    
    
print("\n\nContinue Statement : \n")
for i in range(1,11):
    if(i == 5):
        continue  
    print(i)
    
    
print("\n\nTable of 15 : \n")    
for i in range(1,11):
    print(f"15  X  {i}  =  {15*i}")
          
print("\n\n")
l1 = ["Sachin","Sohan","Vinney","Rohan","Geeta","Sita"] 
for n in l1:
    if n.startswith("S"):
        print("Hello , " + n)      
        
        
print("\n\nPrime Number Checking :  ")
num = int(input("Enter any Number  : "))
i = 2
p = True 
while (i<num):
    if (num%i == 0):
        p = False
        break
    i += 1
    
if(p == True):
    print(f" {num} is a Prime NUmber ")
else:
    print(f" {num} is not a Prime Number ")   
    
    
print("\n\nMy Name is Rahul ",end="")  
print(" Kumar")