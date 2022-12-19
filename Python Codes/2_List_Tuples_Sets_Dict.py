
# List in Python 


print("List in Python :  \n")
a = [34, 56.87, 78, 13, 90]

print(a) 

print(a[1:3])

a.sort() 
print("Sorted List :  ",a)

a.sort()
a.reverse()
a.pop(3)
a.remove(13) 
a.append(99) 
a.insert(2,67)
print("Updated List  :  ",a)


## --> Tuples in Python 

print("\n\nTuples in Python :  \n")
t = (5,7,6,12,56,8,8,8,9)
print(t) 

print("Index of element 8 in Tuple : ",t.index(9))
print("Occurance of 8 in Tuple  : " , t.count(8))



## Dictionary In Python 

print("\n\n Dictionary in Python  \n")
d = {
        "A" : "Hi",
        "B" : "Hello",
        "C" : "Kaise hoo Bhai",
        "D" : "Everything is fine bro !!"
}


print(d)

print(d["B"])

print(type(d))

print("\n Values : ",d.values())
print("\n Dictionary   : ",d.items())

new_d = {
            "Beautiful Girl" : "Not Loyal",
            "Preety Girl " : "Don't carry Character"
}

d.update(new_d)

print("\n\n Updated Dictionary :  ",d)



## Sets in Python 

print("\nSets :  \n")

s = {1,4,5,7,8}

print(s)
print(type(s))

b = set()
print(b)
print(type(b))

print("Length of teh Sets : ",len(s))

s.pop()
print(s)    
s.clear()
print(s)



myDict = { 
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}

print(myDict.values())
print(myDict.keys())

print("\n\n\n\n")
favlang = {}
a = input("Enter for s-1  ")
b = input("Enter for s-2  ")

favlang["s-1"] = a
favlang["s-2"] = b 

print(favlang)