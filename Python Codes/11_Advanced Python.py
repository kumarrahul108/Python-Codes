
## Exception Handling In Python  

try:
   a = int(input("Enter any Number : "))
   c = 1/a
   print(c)
   
except Exception as e:
    print("Exception Occured !!")
    print(e) 
    
else :
    print("We are Successsfull !!")     
    
    
## cUSTOME eXCEPTION : 
    
def increment(num):
    try:
        return int(num)  + 1
    except:
        raise ValueError("Not Good Dear !!!")
    
    
## --> Some Extra Funcyions in Python             
print("\nEnumerate Functions :  \n")
list1 = [3, 53, 2, False, 6.54, "Aryan"]   

print("Index          Values")
for index,item in enumerate(list1):
    print(index," --> ",item)  
    
    

print("\n List Comphrehension : \n")    
a = [2, 5, 8, 78, 15, 19, 56, 203, 854, 123, 67]   

b = [i for i in a if i % 2 == 0] 
print(b)


## LAmbda Function 
print("\n\n Lambda Function : \n")
'''
    def func(a):
        return a + 5

'''

func = lambda a:a+5

x = 555
print(func(x))            


## Join Method 

print("\n\nJoin Method :  ")


list = ["Camera", "Laptop", "iPhone", "iPad", "Hard Disk", "Nvidia Graphics", "1 Tb SSD"]

for item in list:
    print(item," , ",end="")
    
print("\n\n")     
sentence = " <--> ".join(list) 

print(sentence)  


## --> Map
print("\n\nMap Function : \n") 


def square(num):
    return num*num 

l1 = [1,2,3,4,5]

print(l1) 

print(list(map(square,l1)))