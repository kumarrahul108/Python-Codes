'''

Project 1 :  game --> Snake , Water & Gun  

Rule of the Game :  
        Snanke with Water --> Snake Wins
        Snake with Gun --> Gun Wins
        Water with Gun --> Water Wins 

'''


import random  

# -> function for game 

def game(user,comp):   
    
    if(user == comp):
        print("\nMatch is Tied !!")
    
    if(comp == 1):
        if(user == 2):
            print("\n You Loose the Match !!")
        if(user == 3):
            print("\n You Won the Match !!") 
            
    elif(comp == 2):
        if(user == 1):
            print("\n You Won the Match !!") 
        if(user == 3):
            print("\n You Loose the Match !!")
            
    elif(comp == 3):
        if(user == 1):
            print("\n You Loose the Match !!")
        if(user == 2):
            print("\n You Won the Match !!")            
            
            
# game function end here                     

                    
user = int(input("Enter : \n1 : Snake \n2 : Water \n3 : Gun \n      "))
comp = random.randint(1,3)

game(user,comp)

if(comp == 1):
    print("\nComputer Choose  : Snake")
elif(comp == 2):
    print("\nComputer Choose  : Water")
elif(comp == 3):
    print("\nComputer Choose  : Gun")  
    
  
if(user == 1):
    print("\nYou Choose  : Snake")
elif(user == 2):
    print("\nYou Choose  : Water")
elif(user == 3):
    print("\nYou Choose  : Gun")     




