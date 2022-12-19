
## Functions in Python 


def name(n):
    print("Hello , " + n)

name("Rahul")

print("\n")
nm = input("Enter any Name : ")
name(nm)

def conversion(n):
    return n * 2.25

print("Converted Value :  ",conversion(2))   

St = "    Rahul Kumar"
print("Name After Stripping : ",St.strip())  
print("Name AFter Removing  : ",St.replace("Kumar","***"))