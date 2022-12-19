## Files in Python

print("\n Content of the File : \n")

f = open('rk.txt','r')
data = f.read()
print(data)
f.close() 

print("\n")

g = open('rk.txt')
d = g.read(10)  # -> 1st 10 characters
print(d)
g.close() 

print("\n\n Read-Line Operation : \n")
h = open('rk.txt')
d1 = h.readline()  # --> 1 line at a time 
print(d1)
d2 = h.readline()
print(d2)
d3 = h.readline()
print(d3)
h.close() 


r = open('sample.txt','w') 
r.write("New File Creation !!")
r.close() 

r = open('sample.txt','w')
r.write("New File hurrah !")
r.write("\nEnjoying my coding ")
r.close()


print("\n\n Using With Commannd : ")
with open('sample.txt','r') as k:
    content = k.read()
    print(content) 
    

print("\nSensor Content :  \n")   
 
words = ["dokey","dog","fool","chutiya"]      

with open("sensor.txt","r") as f:
    data = f.read()
    print(data)
    f.close() 
    
for wd in words:
    data = data .replace(wd,"**##**")
    with open("sensor.txt","w") as g:
        g.write(data) 
        

print("\n tables : ")

i=1
while (i<=30):
    with open(f"Tables/Multiplication of {i}.txt","w") as f:
        j=1
        while(j<=10):
            f.write(f"{i} X {j} = {i*j}") 
            if (j !=10):
                f.write("\n")
            j += 1
           
    i += 1            
            
    
