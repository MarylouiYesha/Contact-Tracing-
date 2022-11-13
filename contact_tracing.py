#contact tracing

#menu

print("CONTACT TRACING")
print("")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("")



user= int(input (" What do you want to do? (1-3): "))

information= {}


#Option 1
While = True
if user== 1:
    print("Add an item")
    print("")    
        
    name=input("Full Name: ")
    age= int(input("Age: "))
    add=input("Address: ")
    phone= int(input("Phone Number: "))
        
    information[name]=name
    information[age]=age
    information[add]=add
    information[phone]=phone    

    print("Saved!")
    
    
#Option 2
if user==2:
    print("Search")
    
    name2=input("What is your name? ")
    if name2==information[name]:
        print(information[age])
        print(information[add])
        print(information[phone]) 
                
#Option 3
if user==3:
    print("Exit")
    print("")
    exit1=input("Are you sure you want to exit (y/n)? ")
    
    if exit1=="y":
        break
 