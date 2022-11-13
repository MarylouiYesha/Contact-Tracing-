#contact tracing

#menu

print("CONTACT TRACING")
print("")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("")



information= {}




#Option 1
while True:
    user= int(input (" What do you want to do? (1-3): "))
    if user== 1:
        print("Add an item")
        print("")    
        
        name=input("Full Name: ")
        age= int(input("Age: "))
        add=input("Address: ")
        phone= int(input("Phone Number: "))
        
        inputs={
            "Name": name,
            "Age": age,
            "Address": add,
            "Phone": phone
        }  
        
        information[name]=inputs

        print("Saved!")
    
    
#Option 2
    if user==2:
        print("Search")
        name2=input("What is your name? ")
        if name2 in information:
            print(information[name2])
        else:
            print("No record")
                
#Option 3
    if user==3:
        print("Exit")
        print("")
        exit1=input("Are you sure you want to exit (y/n)? ")
  
        if exit1=="y":
            break
 